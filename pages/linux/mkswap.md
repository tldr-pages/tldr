# mkswap

> Set up a Linux swap area on a device or in a file.
> Note: `path/to/file` can either point to a regular file or a swap partition.
> More information: <https://manned.org/mkswap>.

- Set up a given swap area:

`sudo mkswap {{path/to/file}}`

- Check a partition for bad blocks before creating the swap area:

`sudo mkswap -c {{path/to/file}}`

- Specify a label for the partition (to allow `swapon` to use the label):

`sudo mkswap -L {{label}} {{/dev/sda1}}`
