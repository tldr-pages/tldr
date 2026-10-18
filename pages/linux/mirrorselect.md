# mirrorselect

> Select the fastest Gentoo mirrors and update `GENTOO_MIRRORS` in `/etc/portage/make.conf`.
> More information: <https://wiki.gentoo.org/wiki/Mirrorselect>.

- Interactively select source mirrors from a list:

`sudo mirrorselect {{[-i|--interactive]}}`

- Interactively select mirrors from a specific country:

`sudo mirrorselect {{[-i|--interactive]}} {{[-c|--country]}} "{{Germany}}"`

- Automatically select a specific number of the fastest mirrors:

`sudo mirrorselect {{[-s|--servers]}} {{3}}`

- Automatically select the fastest mirrors using a more accurate download test:

`sudo mirrorselect {{[-D|--deep]}} {{[-s|--servers]}} {{3}}`

- Only consider HTTPS mirrors:

`sudo mirrorselect {{[-S|--https]}} {{[-s|--servers]}} {{3}}`

- Print the selected mirrors instead of writing them to `make.conf`:

`mirrorselect {{[-s|--servers]}} {{3}} {{[-o|--output]}}`

- Interactively select an rsync mirror and append it to the repository configuration:

`mirrorselect {{[-i|--interactive]}} {{[-r|--rsync]}} {{[-o|--output]}} | sudo tee -a /etc/portage/repos.conf/gentoo.conf`
