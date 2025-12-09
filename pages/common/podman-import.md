# podman import

> Import a tarball and save it as a filesystem image.
> See also: `podman export`, `podman save`.
> More information: <https://docs.podman.io/en/latest/markdown/podman-import.1.html>.

- Import a tarball from a local file and create an image:

`podman import {{path/to/tarball.tar}} {{image:tag}}`

- Import a tarball from a URL:

`podman import {{https://example.com/image.tar}} {{image:tag}}`

- Import a tarball and add a commit message:

`podman import {{[--message|-m]}} "{{commit_message}}" {{path/to/tarball.tar}} {{image:tag}}`

- Import a tarball and set a default command (required for running the container):

`podman import {{[--change|-c]}} "{{CMD /bin/bash}}" {{path/to/tarball.tar}} {{image:tag}}`

- Import a tarball and set environment variables:

`podman import {{[--change|-c]}} "{{ENV DEBUG=true}}" {{path/to/tarball.tar}} {{image:tag}}`
