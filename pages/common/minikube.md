# minikube

> Tool to run Kubernetes locally.
> More information: <https://github.com/kubernetes/minikube>.

- Start the cluster:

`minikube start`

- Get the IP address of the cluster:

`minikube ip`

- Access a service named my_service exposed via a node port and get the URL:

`minikube service {{my_service}} --url`

- Open the Kubernetes dashboard in a browser:

`minikube dashboard`

- Stop the running cluster:

`minikube stop`

- Delete the cluster:

`minikube delete`
