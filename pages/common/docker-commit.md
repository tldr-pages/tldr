# docker commit

> Create a new image from a container's changes.
> More information: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Create an image from a specific container:

`docker commit {{container}} {{image}}:{{tag}}`

- Apply a `CMD` Dockerfile instruction to the created image:

`docker commit {{[-c|--change]}} "CMD {{command}}" {{container}} {{image}}:{{tag}}`

- Apply an `ENV` Dockerfile instruction to the created image:

`docker commit {{[-c|--change]}} "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Create an image with a specific author in the metadata:

`docker commit {{[-a|--author]}} "{{author}}" {{container}} {{image}}:{{tag}}`

- Create an image with a specific comment in the metadata:

`docker commit {{[-m|--message]}} "{{comment}}" {{container}} {{image}}:{{tag}}`

- Create an image without pausing the container during commit:

`docker commit {{[-p|--pause]}} {{false}} {{container}} {{image}}:{{tag}}`

- Display help:

`docker commit --help`
