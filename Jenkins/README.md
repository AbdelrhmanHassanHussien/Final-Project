# Jenkins Pipelines

This repository contains Jenkins pipelines for different parts of the application and infrastructure management process. The pipelines utilize a shared library from the following repository: [Jenkins Shared Library](https://github.com/AbdelrhmanHassanHussien/Jenkins-Shared-Library).

## SSDLC Integration
- The Jenkins pipelines incorporate SSDLC principles by applying the "shift-left" approach, which integrates security testing early in the development lifecycle. This proactive method helps address vulnerabilities before they reach production. 
- Key security measures include code linting, static application security testing, and Docker image scanning
## Credential Management
- **Credentials Storage**: Use Jenkins’ credentials management to securely store sensitive information like API keys and passwords.
- **Environment Variables**: Access credentials via environment variables configured in Jenkins.

## Security Authorization
- **Mixed Security Authorization**: Segment access permissions based on roles and responsibilities.
- **Least Privilege Principle**: Ensure users and services have only the permissions needed for their tasks.

## Plugin Installation

### Required Plugins
1. **AWS Credentials Plugin**: For managing AWS credentials in Jenkins.
2. **GitHub Plugin**: For integrating Jenkins with GitHub repositories.

#### Install Plugins
1. Go to **Manage Jenkins** -> **Manage Plugins**.
2. Under the **Available** tab, search for **AWS Credentials**, **AWS Steps**, and **GitHub**.
3. Select the plugins and click **Install without Restart**.

## Jenkins Shared Library

The pipelines in this repository make use of a shared library to promote reusable and modular pipeline steps. The shared library is hosted in the following GitHub repository: [Jenkins Shared Library](https://github.com/AbdelrhmanHassanHussien/Jenkins-Shared-Library).

To use the shared library in your Jenkins pipeline, add the following configuration to your `Jenkinsfile`:

```groovy
@Library('Jenkins-Shared-Library') _
// Pipeline Code
```


## Jenkins Pipelines

**App_Pipeline**: Pipeline responsible for building, testing, and deploying the application.
- Checkout SCM Stage
- Linter Stage
- SAST Stage
- App Unit Testing Stage
- Build Image & Scanning
- Login & Push Image
- Deployment Stage
- Post Actions & cleanup Stage

**Remove_Deployment**: Pipeline responsible for tearing down or removing the deployment from the environment.
- Checkout SCM Stag
- Remove Deployment Stage
- Post Actions & cleanup Stage

**Infra_Pipeline**: It is responsible for both **applying** and **destroying** infrastructure resources by using **Build with Parameters** action: (apply or destroy)
- Checkout SCM Stage
- IaS Scanning
- Initialize Terraform Stage
- Terraform Validate Stage
- Terraform Plan Stage
- Terraform Apply/Destroy Stage
- Post Actions & cleanup Stage

## Setup WebHook

### Configure WebHook in GitHub:
1. Go to your GitHub repository's **Settings** -> **Webhooks** -> **Add Webhook**.
2. Set the "Payload URL" to `http://your-jenkins-server/github-webhook/`.
3. Set content type to `application/json`.
4. Choose **Just the push event** and click **Add Webhook**.

### Enable WebHook in Jenkins:
1. In your Jenkins job, under **Build Triggers**, select **GitHub hook trigger for GITScm polling**.
2. Ensure Jenkins is configured with the GitHub plugin to receive webhooks.


## How to Run the Pipelines
1. Configure Jenkins Shared Library under **Manage Jenkins** -> **Configure System** -> **Global Pipeline Libraries**.
2. Update your `Jenkinsfile` to use the shared library.
3. Trigger pipelines through Jenkins UI or set automated SCM-based triggers.