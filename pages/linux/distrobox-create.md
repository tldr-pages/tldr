# distrobox-create

> Create a distrobox container. More about distrobox: `tldr distrobox`.
> The created container will be tightly integrated with the host, allowing sharing of the HOME directory of the user, external storage, external usb devices and graphical apps (X11/Wayland), and audio.
> More information: <https://github.com/89luca89/distrobox/blob/main/docs/usage/distrobox-create.md>.

- Create a distrobox using the Ubuntu Linux image:

`distrobox-create {{container_name}} --image {{ubuntu:latest}}`

- Clone a distrobox container:

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
