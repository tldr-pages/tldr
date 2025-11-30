# docker context

> Switch between contexts to manage multiple Docker environments.
> More information: <https://docs.docker.com/reference/cli/docker/context/>.

- Create a context using a specific Docker endpoint:

`docker context create {{my_context}} --docker "host={{tcp://remote-host:2375}}"`

- Create a context based on the `$DOCKER_HOST` environment variable:

`docker context create {{my_context}}`

- Switch to a context:

`docker context use {{my_context}}`

- List all contexts:

`docker context ls`
