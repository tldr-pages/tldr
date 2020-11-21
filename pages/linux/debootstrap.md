# debootstrap

> Create a basic Debian system.
> More information: <https://wiki.debian.org/Debootstrap>.

- Create a Debian buster system inside {{buster-chroot}} directory:

`sudo debootstrap buster {{path/to/buster-chroot/}} http://deb.debian.org/debian`

- Create an Ubuntu 20.04 system inside {{focal-root}} directory with local mirror:

`sudo debootstrap focal {{path/to/focal-root/}} {{file:///path/to/mirror/}}`

- Switch to a bootstrapped system:

`sudo chroot {{path/to/root}}`
