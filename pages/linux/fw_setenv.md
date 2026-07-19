# fw_setenv

> Modify U-Boot environment variables from Linux userspace.
> See also: `fw_printenv`.
> More information: <https://manned.org/fw_setenv>.

- Set or update an environment variable:

`fw_setenv {{name}} {{value}}`

- Delete an environment variable:

`fw_setenv {{name}}`

- Use a specific configuration file:

`fw_setenv {{[-c|--config]}} {{path/to/fw_env.config}} {{name}} {{value}}`

- Apply multiple variable changes from a script file:

`fw_setenv {{[-s|--script]}} {{path/to/script}}`
