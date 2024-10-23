# Start minikube with different configurations

More information: <https://minikube.sigs.k8s.io/docs/>.

- Start `minikube` with a specific Kubernetes version:

  `minikube start --kubernetes-version={{v1.24.0}}`

- Start `minikube` with a specific resource allocation:

  `minikube start --memory={{2048}} --cpus={{2}}`

- Start `minikube` with a specific driver:

  `minikube start --driver={{virtualbox}}`

- Start `minikube` in the background (headless mode):

  `minikube start --background`

- Start `minikube` with custom add-ons:

  `minikube start --addons={{metrics-server}}`
