# rmmod

> Remove modules from the Linux kernel.
> More information: <https://manned.org/rmmod>.

- Remove a module from the kernel:

`sudo rmmod {{module_name}}`

- Remove a module from the kernel and display verbose information:

`sudo rmmod --verbose {{module_name}}`

- Remove a module from the kernel and send errors to syslog instead of `stderr`:

`sudo rmmod --syslog {{module_name}}`

- Display help:

`rmmod --help`

- Display version:

`rmmod --version`
