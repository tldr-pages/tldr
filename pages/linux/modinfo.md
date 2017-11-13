# modinfo

> Extract information about a Linux kernel module.

- List all attributes of a kernel module:

`modinfo {{kernel_module}}`

- List value(s) of the specified field(s) instead of all the fields:

`modinfo -F {{author|description|license|parm|filename}} {{kernel_module}}`
