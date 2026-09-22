# podman commit

> Create a new image based on the changed container.
> More information: <https://docs.podman.io/en/latest/markdown/podman-commit.1.html>.

- Create an image from a specific container:

`podman commit {{container}} {{image}}:{{tag}}`

- Apply an `ENV` instruction to the created image:

`podman commit {{[-c|--change]}} "ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Apply `LABEL`, `ENTRYPOINT` and `CMD` instruction to the created image:

`podman commit {{[-c|--change]}} CMD={{command}} {{[-c|--change]}} ENTRYPOINT={{command}} {{[-c|--change]}} "LABEL {{key}}={{value}}" {{container}} {{image}}:{{tag}}`

- Create an image with a specific author and comment in the metadata:

`podman commit {{[-a|--author]}} "{{author}}" {{[-m|--message]}} "{{comment}}" {{container}} {{image}}:{{tag}}`

- Create an image without pausing the container during commit:

`podman commit {{[-p|--pause]}} false {{container}} {{image}}:{{tag}}`

- Display help:

`podman commit --help`
