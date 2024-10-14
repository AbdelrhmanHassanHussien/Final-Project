#!/bin/bash

set -e

# Update the system
echo "Updating the system..."
sudo apt update -y && sudo apt upgrade -y

# Install essential packages
echo "Installing essential packages..."
sudo apt install -y curl python3 python3-pip

# Install Docker
echo "Installing Docker..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
sudo apt install -y docker-ce
sudo usermod -aG docker "${USER}"

# Install AWS CLI
echo "Installing AWS CLI..."
sudo snap install aws-cli --classic

# Install kubectl
echo "Installing kubectl..."
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.2/2024-07-12/bin/linux/amd64/kubectl
sudo chmod +x ./kubectl
mkdir -p "$HOME/bin"
sudo cp ./kubectl "$HOME/bin/kubectl"
export PATH="$HOME/bin:$PATH"

# Install Terraform
echo "Installing Terraform..."
sudo snap install terraform --classic

# Install Java
echo "Installing Java..."
sudo apt install -y fontconfig openjdk-17-jre

# Install Jenkins
echo "Installing Jenkins..."
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install -y jenkins
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
sudo systemctl restart docker

# Install Python 3.12 venv
echo "Installing Python 3.12 venv..."
sudo apt install -y python3.12-venv libffi-dev python3-dev build-essential

# Verify installations
echo "Verifying installations..."
docker --version
jenkins --version
terraform --version
aws --version
kubectl version --client
java -version

