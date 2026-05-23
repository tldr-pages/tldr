# mirrorselect

> Select `GENTOO_MIRRORS` and the Gentoo rsync mirror.
> More information: <https://wiki.gentoo.org/wiki/Mirrorselect>.

- Select distfiles mirrors interactively and update Portage configuration:

`sudo mirrorselect -i`

- Select distfiles mirrors interactively from a specific country:

`sudo mirrorselect -i -c "{{United States (USA)}}"`

- Automatically select a number of distfiles mirrors with deep speed testing:

`sudo mirrorselect -s {{3}} -b {{10}} -D`

- Print selected distfiles mirrors to `stdout` instead of updating the configuration:

`mirrorselect -s {{3}} -b {{10}} -o`

- Select an rsync mirror interactively and append it to the Gentoo repository configuration:

`sudo sh -c 'mirrorselect -i -r -o >> {{/etc/portage/repos.conf/gentoo.conf}}'`
