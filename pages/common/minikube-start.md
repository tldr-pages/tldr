# minikube-start

> Start minikube with different configurations.
> More information: <https://minikube.sigs.k8s.io/docs/>.

- Start Minikube with Specific Kubernetes Version:

`minikube start --kubernetes-version=v1.24.0`

- Start Minikube with Custom Resource Allocation:

`minikube start --memory=2048 --cpus=2`

- Start Minikube with a Specific Driver:

`minikube start --driver=virtualbox`

- Start Minikube in Background (Headless Mode):

`minikube start --background`

- Start Minikube with Custom Addons:

`minikube start --addons=metrics-server`

