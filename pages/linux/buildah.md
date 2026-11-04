# buildah

> Build OCI container images without a container daemon.
> Works without root and is commonly used together with `podman`.
> More information: <https://github.com/containers/buildah/blob/main/docs/buildah.1.md>.

- Create a working container from an image:

`buildah from {{image}}`

- Build an image from a Containerfile:

`buildah build {{[-t|--tag]}} {{image:tag}} {{path/to/context}}`

- List working containers:

`buildah containers`

- Run a command inside a working container:

`buildah run {{container}} {{command}}`

- Mount a working container's root filesystem and print the mount point:

`buildah mount {{container}}`

- Unmount a working container:

`buildah umount {{container}}`

- Commit a working container as a new image:

`buildah commit {{container}} {{image:tag}}`

- Push an image to a registry:

`buildah push {{image:tag}} docker://{{registry_hostname}}/{{image:tag}}`
