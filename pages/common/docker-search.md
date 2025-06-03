# docker search

> Search for Docker images on Docker Hub.
> More information: [https://docs.docker.com/reference/cli/docker/search/](https://docs.docker.com/reference/cli/docker/search/).

* Search for Docker images by name or keyword:

`docker search {{keyword}}`

* Search for images and only show official ones:

`docker search --filter {{is-official=true}} {{keyword}}`

* Search for images and only show automated builds:

`docker search --filter {{is-automated=true}} {{keyword}}`


* Search for images and limit the number of results:

`docker search --limit {{number}} {{keyword}}`

