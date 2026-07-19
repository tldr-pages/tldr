# fw_printenv

> Print U-Boot environment variables from Linux userspace.
> See also: `fw_setenv`.
> More information: <https://manned.org/fw_printenv>.

- Print the entire U-Boot environment:

`fw_printenv`

- Print specific environment variables:

`fw_printenv {{bootcmd bootargs ...}}`

- Use a specific configuration file:

`fw_printenv {{[-c|--config]}} {{path/to/fw_env.config}}`
