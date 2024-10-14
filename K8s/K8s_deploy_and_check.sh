#!/bin/bash

# Define the namespace to check
NAMESPACE="project"

# Apply Kubernetes manifests
echo "Applying namespace.yaml..."
kubectl apply -f namespace.yaml

echo "Applying pv.yaml..."
kubectl apply -f pv.yaml

echo "Applying pvc.yaml..."
kubectl apply -f pvc.yaml

echo "Applying job.yaml..."
kubectl apply -f job.yaml

echo "Applying service.yaml..."
kubectl apply -f service.yaml

echo "Applying ingress.yaml..."
kubectl apply -f ingress.yaml

echo "Applying deployment.yaml..."
kubectl apply -f deployment.yaml

# Wait for a few seconds to ensure resources are created
echo "Waiting for resources to be created..."
sleep 30

# Check if all pods are running
echo "Checking the status of pods in the namespace '$NAMESPACE'..."
PODS_STATUS=$(kubectl get pods -n $NAMESPACE --no-headers | awk '{print $3}' | sort | uniq)

if [[ $PODS_STATUS == "Running" ]]; then
  echo "All pods are running successfully."
else
  echo "Some pods are not running. Here is the status:"
  kubectl get pods -n $NAMESPACE
fi

# Optional: Check other resources if needed
echo "Checking services..."
kubectl get services -n $NAMESPACE

echo "Checking deployments..."
kubectl get deployments -n $NAMESPACE

echo "Checking ingress..."
kubectl get ingress -n $NAMESPACE
