# mirrorselect

> Select optimal Gentoo download and rsync mirrors.
> More information: <https://wiki.gentoo.org/wiki/Mirrorselect>.

- Open an interactive TUI to select download mirrors:

sudo mirrorselect --interactive

- Open an interactive TUI filtered by country:

sudo mirrorselect --interactive --country {{country}}

- Select the fastest download mirrors based on download speed:

sudo mirrorselect --servers {{4}}

- Select mirrors and append the configuration to Portage:

sudo mirrorselect --interactive --output >> /etc/portage/make.conf

- Select rsync mirrors and append the configuration to Portage:

sudo mirrorselect --interactive --rsync --output >> /etc/portage/make.conf
