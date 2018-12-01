# kompose

> A tool to convert docker-compose applications to Kubernetes.

- Deploy a dockerized application to Kubernetes:

`kompose up -f {{docker-compose.yml}}`

- Delete instantiated services/deployments from Kubernetes:

`kompose down -f {{docker-compose.yml}}`

- Convert a docker-compose file into Kubernetes resources file:

`kompose convert -f {{docker-compose.yml}}`
