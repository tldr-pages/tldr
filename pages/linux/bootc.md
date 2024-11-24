# bootc

> Boot and upgrade via container images.
> Manages transactional, in-place operating system updates using OCI/Docker container images.
> More information: <https://containers.github.io/bootc/>.

- Show deployments in the order they will appear in the bootloader:

`bootc status`

- Check if any updates are available:

`bootc upgrade --check`

- Prepare a new update and reboot into it:

`bootc upgrade --apply`

- Change OS base to new container image:

`bootc switch {{image}}`

- Reboot into the previous ostree deployment:

`bootc rollback`
