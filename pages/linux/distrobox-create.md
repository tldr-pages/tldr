# distrobox-create

> Create a Distrobox container. See also: `tldr distrobox`.
> The container created will be tightly integrated with the host, allowing sharing of the user's HOME directory, external storage, external USB devices, graphical apps (X11/Wayland), and audio.
> More information: <https://distrobox.it/usage/distrobox-create>.

- Create a Distrobox container using the Ubuntu image:

`distrobox-create {{container_name}} --image {{ubuntu:latest}}`

- Clone a Distrobox container:

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
