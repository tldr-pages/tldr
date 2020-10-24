# modinfo

> Extract information about a Linux kernel module.

- List all attributes of a kernel module:

`modinfo {{kernel_module}}`

- List the specified attribute only:

`modinfo -F {{author|description|license|parm|filename}} {{kernel_module}}`
