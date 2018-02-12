# mkswap

> Sets up a Linux swap area on a device or in a file.

- Setup a given partition as swap area:

`sudo mkswap {{/dev/sdb7}}`

- Use a given file as swap area:

`sudo mkswap {{path/to/file}}`

- Check a partition for bad blocks before creating the swap area:

`sudo mkswap -c {{/dev/sdb7}}`

- Specify a label for the file (to allow `swapon` to use the label):

`sudo mkswap -L {{swap1}} {{path/to/file}}`
