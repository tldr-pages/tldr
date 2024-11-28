# bootc switch

> Target a new container image reference to boot.
> More information: <https://containers.github.io/bootc/man/bootc-switch.html>.

- Change OS base to a new container image from a registry:

`sudo bootc switch {{image}}`

- Change OS base to a new container image from the local image storage of the root user:

`sudo bootc switch --transport containers-storage {{image}}`

- Change OS base to a new container image stored in a tarball:

`sudo bootc switch --transport oci-archive {{path/to/image.tar.gz}}`
