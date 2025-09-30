# docker images

> Manage Docker images.
> More information: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- List all Docker images:

`docker images`

- List all Docker images including intermediates:

`docker images {{[-a|--all]}}`

- List the output in quiet mode (only numeric IDs):

`docker images {{[-q|--quiet]}}`

- List all Docker images not used by any container:

`docker images {{[-f|--filter]}} dangling=true`

- List images that contain a substring in their name:

`docker images "{{*name*}}"`

- Sort images by size:

`docker images --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
