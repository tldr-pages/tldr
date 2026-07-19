# mirrorselect

> Select Gentoo download and rsync mirrors with a TUI or automated probes.
> More information: <https://wiki.gentoo.org/wiki/Mirrorselect>.

- Open an interactive interface for mirror selection:

`sudo mirrorselect -i`

- Open an interactive interface limited to a specific country:

`sudo mirrorselect -i -c "{{United States (USA)}}"`

- Automatically pick the 3 fastest mirrors by download speed:

`mirrorselect -s3 -b10 -D`

- Open an interactive interface to choose an rsync mirror:

`sudo mirrorselect -i -r`

- Write selected GENTOO_MIRRORS into make.conf:

`sudo mirrorselect -i -o >> /etc/portage/make.conf`
