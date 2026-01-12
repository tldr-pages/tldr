# docker image ls

> List Docker images.
> More information: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- List all Docker images:

`docker {{[images|image ls]}}`

- List all Docker images including intermediates:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- List the output in quiet mode (only numeric IDs):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- List all Docker images not used by any container:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- List images that contain a substring in their name:

`docker {{[images|image ls]}} "{{*name*}}"`

- Sort images by size:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
