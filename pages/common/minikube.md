# minikube

> Run Kubernetes on your local machine for free.

- Start the cluster:

`minikube start`

- View the cluster details:

`kubectl cluster-info`

- View the nodes in the cluster:

`kubectl get nodes`

- Acess a service exposed via a node port:

`minikube service [-n {{NAMESPACE}}] [--url] {{NAME}}`

- Open kubernetes dashboard in a browser:
 
`minikube dashboard`


 
 
