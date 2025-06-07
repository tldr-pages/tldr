# mkswap

> Set up a Linux swap area on a device or in a file.
> Note: `path/to/file` can either point to a regular file or a swap partition.
> More information: <https://manned.org/mkswap>.

- Set up a given swap area:

`sudo mkswap {{path/to/file}}`

- Check a partition for bad blocks before creating the swap area:

`sudo mkswap {{[-c|--check]}} {{path/to/file}}`

- Specify a label for the partition (to allow `swapon` to use the label):

`sudo mkswap {{[-L|--label]}} {{label}} {{/dev/sdXY}}`

- Use the specified UUID:

`sudo mkswap {{[-U|--uuid]}} {{clear|random|time|UUID_value}}`

- Set up a swap file (for btrfs, see `tldr btrfs filesystem` instead):

`sudo mkswap {{[-s|--size]}} {{file_size}} {{[-F|--file]}} {{path/to/swapfile}}`
