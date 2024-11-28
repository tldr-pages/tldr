# incus

> Modern, secure and powerful system container and virtual machine manager.
> More information: <https://linuxcontainers.org/incus/docs/main>.

- List all containers and virtual machines (both running and stopped):

`incus list`

- Create a container from an image, with a custom name:

`incus create {{image}} {{container_name}}`

- Start or stop an existing container:

`incus {{start|stop}} {{container_name}}`

- Open a shell inside an already running container:

`incus shell {{container_name}}`

- Remove a stopped container:

`incus delete {{container_name}}`

- Pull an image from an image repository (remote) to local:

`incus copy {{remote}}:{{image}} local:{{custom_image_name}}`

- List all available images in the official `images:` remote:

`incus image list images:`

- List all images already downloaded to the `local:` remote:

`incus image list local:`
