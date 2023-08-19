# swapoff

> Disable devices and files for swapping.
> Note: `path/to/file` can either point to a regular file or a swap partition.
> More information: <https://manned.org/swapoff>.

- Disable a given swap area:

`swapoff {{path/to/file}}`

- Disable all swap areas in `/proc/swaps`:

`swapoff --all`

- Disable a swap partition by its label:

`swapoff -L {{label}}`
