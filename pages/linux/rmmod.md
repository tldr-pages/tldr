# rmmod

> Remove modules from the Linux kernel.
> More information: <https://manned.org/rmmod>.

- Remove a module from the kernel:

`sudo rmmob {{module_name}}`

- Remove a module from the kernel and display verbose information:

`sudo rmmob --verbose {{module_name}}`

- Remove a module from the kernel and send errors to syslog instead of standard error:

`sudo rmmob --syslog {{module_name}}`

- Display help:

`rmmob --help`

- Display version:

`rmmob --version`
