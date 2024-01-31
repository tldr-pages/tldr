# getconf

> Get configuration values from your Linux system.
> More information: <https://manned.org/getconf.1>.

- List [a]ll configuration values available:

`getconf -a`

- List the configuration values for a specific directory:

`getconf -a {{path/to/directory}}`

- Check if your linux system is a 32-bit or 64-bit:

`getconf LONG_BIT`

- Check how many processes the current user can run at once:

`getconf CHILD_MAX`

- List every configuration value and then find patterns with the `grep` command (i.e every value with MAX in it):

`getconf -a | grep MAX`
