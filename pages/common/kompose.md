# kompose

> Kompose is a tool to help users who are familiar with docker-compose move to Kubernetes.

- Deploy your Dockerized application to a container orchestrator:

`kompose up -f {{docker-compose.yml}}`

- Delete instantiated services/deployment from kubernetes:

`kompose down -f {{docker-compose.yml}}`

- Convert a Docker Compose file into Kubernetes resources file: 

`kompose convert -f {{docker-compose.yml}}`
