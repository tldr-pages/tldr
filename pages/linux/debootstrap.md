# debootstrap

> Create a basic Debian system.
> More information: <https://wiki.debian.org/Debootstrap>.

- Create a Debian stable release system inside the `debian-root` directory:

`sudo debootstrap stable {{path/to/debian-root/}} http://deb.debian.org/debian`

- Create a minimal system including only required packages:

`sudo debootstrap --variant=minbase stable {{path/to/debian-root/}}`

- Create an Ubuntu 20.04 system inside the `focal-root` directory with a local mirror:

`sudo debootstrap focal {{path/to/focal-root/}} {{file:///path/to/mirror/}}`

- Switch to a bootstrapped system:

`sudo chroot {{path/to/root}}`

- List available releases:

`ls /usr/share/debootstrap/scripts/`
