# docker-slim

> Analyze and optimize Docker images.
> More information: <https://github.com/docker-slim/docker-slim>.

- Start DockerSlim on interactive mode:

`docker-slim`

- Analyze Docker layers from a specific image:

`docker-slim xray --target {{image:tag}}`

- Lint a Dockerfile:

`docker-slim lint --target {{path/to/Dockerfile}}`

- Analyze and generate an optimized Docker image:

`docker-slim build {{image:tag}}`

- Display help for a subcommand:

`docker-slim {{subcommand}} --help`
