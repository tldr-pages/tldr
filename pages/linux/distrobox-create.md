# distrobox create

> Create a Distrobox container.
> The created container is integrated with the host and can share the user's `$HOME` directory, external storage, USB devices, graphical apps (X11/Wayland), and audio.
> See also: `distrobox`.
> More information: <https://distrobox.it/usage/distrobox-create/>.

- Create a container from the Ubuntu image:

`distrobox create {{[-n|--name]}} {{container_name}} {{[-i|--image]}} {{ubuntu:latest}}`

- Clone an existing container:

`distrobox create {{[-c|--clone]}} {{container_name}} {{[-n|--name]}} {{cloned_container_name}}`

- Create a container with its own home directory:

`distrobox create {{[-n|--name]}} {{container_name}} {{[-i|--image]}} {{image}} {{[-H|--home]}} {{path/to/directory}}`

- Pull the image and create a container without asking:

`distrobox create {{[-Y|--yes]}} {{[-p|--pull]}} {{[-n|--name]}} {{container_name}} {{[-i|--image]}} {{image}}`

- Display help:

`distrobox create {{[-h|--help]}}`
