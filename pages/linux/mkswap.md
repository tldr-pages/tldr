# mkswap

> Sets up a Linux swap area on a device or in a file.

- Setup /dev/sdb7 as swap area:

`sudo mkswap {{/dev/sdb7}}`

- Use a given file as swap area:

`sudo mkswap {{path/to/file}}`

- Check /dev/sdb7 for bad blocks before creating the swap area:

`sudo mkswap -c {{/dev/sdb7}}`

- Specify a label for the file:

`sudo mkswap -L {{swap1}} {{/path/to/file}}`
