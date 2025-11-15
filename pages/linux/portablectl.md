# portablectl

> A systemd utility for managing and deploying portable service images on Linux systems.
> More information: <https://www.freedesktop.org/software/systemd/man/portablectl.html>.

- List available portable service images discovered in the portable image search paths:

`portablectl list`

- Attach a portable service image to the host system:

`portablectl attach {{path/to/image}}`

- Detach a portable service image from the host system:

`portablectl detach {{path/to/image|image_name}}`

- Display details and metadata about a specified portable service image:

`portablectl inspect {{path/to/image}}`

- Check if a portable service image is attached to the host system:

`portablectl is-attached {{path/to/image|image_name}}`
