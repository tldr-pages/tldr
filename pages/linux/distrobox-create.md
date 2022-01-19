# distrobox-create

> Create Distrobox containers with an input name and image.
> The created container will be tightly integrated with the host, allowing sharing of the HOME directory of the user, external storage, external usb devices and graphical apps (X11/Wayland), and audio.
> More information: <https://distrobox.privatedns.org>.

- Create a distrobox using the Alpine image:

`distrobox-create {{container_name}} --image alpine`

- Clone a distrobox:

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
