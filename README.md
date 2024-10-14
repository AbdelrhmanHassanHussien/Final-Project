# **DevOps Project - Django Application with Docker, Kubernetes, Terraform, AWS, and Jenkins CI/CD**

## **Overview**

This repository showcases a comprehensive DevOps project designed to deploy a Django application using a range of modern tools and practices. The project integrates several technologies to achieve a robust, scalable, and automated deployment pipeline.

### **Project Components**

- **Django**: A high-level Python web framework used for building the application. Django provides a clean, pragmatic design and a robust set of features for web development.

- **Docker**: Used for containerizing the Django application. The Docker setup includes single and multi-stage builds to ensure efficient and secure image creation.

- **Kubernetes (K8s)**: Manages the deployment, scaling, and operation of the containerized application. Kubernetes provides automated container orchestration, ensuring the application is resilient and scalable.

- **Terraform**: Automates the provisioning of cloud infrastructure on AWS. Terraform scripts are used to define and manage AWS resources such as Virtual Private Clouds (VPCs), subnets, and Elastic Kubernetes Service (EKS) clusters.

- **Jenkins**: Implements Continuous Integration and Continuous Deployment (CI/CD) pipelines to automate the build, test, and deployment processes. Jenkins pipelines integrate with Docker, Kubernetes, and Terraform to streamline development and deployment workflows.

- **Prometheus**: Deployed on the EKS cluster to collect and store metrics from the application and the underlying infrastructure. Prometheus provides powerful querying capabilities and is used for monitoring system performance and health.

- **Grafana**: Deployed alongside Prometheus on the EKS cluster to visualize metrics collected by Prometheus. Grafana is used to create dashboards and visualizations to monitor application performance and gain insights from the collected data.


**Clone the Repository**

   ```bash
   git clone https://github.com/AbdelrhmanHassanHussien/Final-Project.git
```