terraform {
  backend "s3" {
    bucket                  = "terraform-FinalProject"
    key                     = "filekey"
    region                  = "us-east-2"
  }
}
provider "aws" {
  region = "us-east-2"
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical's AWS account ID for Ubuntu
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

module "vpc" {
  source         = "./VPC_Module"
  cidr_block     = "10.0.0.0/16"
  vpc_name       = "VPC"
  public_subnets = ["10.0.1.0/24", "10.0.3.0/24"]
  private_subnets = ["10.0.2.0/24", "10.0.4.0/24"]
  azs            = ["us-east-2a", "us-east-2b"]
}

module "security_group" {
  source  = "./SecurityGroup_Module"
  sg_name = "Security-Group"
  vpc_id  = module.vpc.vpc_id
}

module "eks" {
  source = "./EKS_Module"
  vpc_id              = module.vpc.vpc_id
  sg_id               = module.security_group.security_group_id
  cluster_name        = "eks-cluster"
  private_subnet_ids  = module.vpc.private_subnets[*]
  kubernetes_version  = "1.30" 
}

module "nodegroup" {
  source = "./NodeGroup_Module"
  cluster_name        = module.eks.cluster_name
  node_group_name     = "eks-node-group"
  private_subnet_ids  = module.vpc.private_subnets[*]
  instance_types      = ["t3.medium"]
  desired_size        = 1
  max_size            = 1
  min_size            = 1
}


module "ec2_instance" {
  source           = "./EC2_Module"
  ami_id           = data.aws_ami.ubuntu.id  # Replace with actual AMI ID
  instance_type    = "t2.micro"
  subnet_id        = module.vpc.public_subnets[0]  # Deploying in the first public subnet
  security_group_id = module.security_group.security_group_id
  key_name         = "projectkey"  # Replace with your actual key pair name
  instance_name    = "EC2-Bastion "
}