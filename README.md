# Flask ArgoCD Example

![CI](https://github.com/dfratte/flask-argo-example/actions/workflows/test.yaml/badge.svg)

A simple Flask web application deployed on a Kubernetes cluster using ArgoCD.

## Features
- Simple Flask web server responding with "Hello, World!"
- Dockerized for easy deployment
- Kubernetes manifests for deployment and service
- GitOps workflow using ArgoCD

## Prerequisites
Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes (k3s or minikube)](https://kubernetes.io/docs/setup/)
- [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Project Structure
```
.
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build instructions
├── k8s/
│   ├── deployment.yaml   # Kubernetes deployment
│   ├── service.yaml      # Kubernetes service
├── argocd-application.yaml  # ArgoCD application configuration
└── README.md             # Project documentation
```

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/python-hello-world.git
cd python-hello-world
```

### 2. Build and Run Locally (Optional)
You can test the application locally using Docker:
```sh
docker build -t flask-argo-example:latest .
docker run -p 5000:5000 flask-argo-example:latest
```
Then, visit `http://localhost:5000` in your browser.

### 3. Deploy to Kubernetes using ArgoCD

#### Step 1: Push to GitHub
Ensure your code and Kubernetes manifests are in a Git repository.
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

#### Step 2: Apply ArgoCD Application
Apply the ArgoCD application manifest:
```sh
kubectl apply -f argocd-application.yaml
```

#### Step 3: Sync in ArgoCD UI
- Open ArgoCD dashboard (`http://localhost:8080` or wherever it is exposed)
- Find `python-hello-world`
- Click **Sync** to deploy

### 4. Access the Application
Once deployed, access the application:

- **If using NodePort**: `http://<node-ip>:<node-port>`
- **If using Ingress**: `http://<your-domain>`

## Troubleshooting
If you encounter issues:
- Check pod logs: `kubectl logs -l app=python-hello-world`
- Describe pod status: `kubectl describe pod <pod-name>`
- Verify ArgoCD sync status in the UI

---

Made with ❤️ by Daniel Fratte