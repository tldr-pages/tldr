# debootstrap

> Create a basic Debian system.
> More information: <https://wiki.debian.org/Debootstrap>.

- Create a Debian stable release system inside the `debian-root` directory:

`sudo debootstrap stable {{path/to/debian-root}}/ http://deb.debian.org/debian`

- Create a minimal system including only required packages:

`sudo debootstrap --variant=minbase stable {{path/to/debian-root}}/`

- Create a Debian Unstable system inside the `sid-root` directory with a local mirror:

`sudo debootstrap sid {{path/to/sid-root}}/ {{file:///path/to/mirror}}/`

- Switch to a bootstrapped system:

`sudo chroot {{path/to/root}}`

- List available releases:

`ls /usr/share/debootstrap/scripts/`
