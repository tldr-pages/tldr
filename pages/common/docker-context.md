# docker context

> Lets you switch between contexts to manage multiple Docker environments.

- Create context using a specific Docker endpoint:

`docker context create my-context --docker "host=tcp://remote-host:2375"`

- Create based on DOCKER_HOST environment variable:

`docker context create my-context`

- Switch to a context:

`docker context use my-context`

- List all contexts:

`docker context ls`
