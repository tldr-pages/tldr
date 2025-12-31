# swapon

> Enable devices and files for swapping.
> Note: `path/to/file` can either point to a regular file or a swap partition.
> More information: <https://manned.org/swapon.8>.

- Show swap information:

`swapon`

- Enable a given swap area:

`sudo swapon {{path/to/file}}`

- Enable all swap areas specified in `/etc/fstab` except those with the `noauto` option:

`sudo swapon {{[-a|--all]}}`

- Enable a swap partition by its label:

`sudo swapon -L {{label}}`
