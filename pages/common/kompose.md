# kompose

> Convert docker-compose applications to Kubernetes.
> More information: <https://github.com/kubernetes/kompose>.

- Deploy a dockerized application to Kubernetes:

`kompose up {{[-f|--file]}} {{docker-compose.yml}}`

- Delete instantiated services/deployments from Kubernetes:

`kompose down {{[-f|--file]}} {{docker-compose.yml}}`

- Convert a docker-compose file into Kubernetes resources file:

`kompose convert {{[-f|--file]}} {{docker-compose.yml}}`
