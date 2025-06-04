# docker search

> Search for Docker images on Docker Hub.
> More information: <https://docs.docker.com/reference/cli/docker/search/>.

- Search for Docker images by name or keyword:

`docker search {{keyword}}`

- Search for images and only show official ones:

`docker search {{[-f|--filter]}} is-official={{true}} {{keyword}}`

- Search for images and only show automated builds:

`docker search {{[-f|--filter]}} is-automated={{true}} {{keyword}}`

- Search for images with a minimum number of stars:

`docker search --filter {{stars=NUMBER}} {{keyword}}`

- Limit the number of results:

`docker search --limit {{number}} {{keyword}}`

- Customize the output format:

`docker search --format "{{.Name}}: {{.Description}}" {{keyword}}`
