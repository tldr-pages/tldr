# getconf

> getconf - get configuration values from your Linux system.
> 

- List every configuration values available

`getconf -a`

- List the configuration values for a specific directory

`getconf -a {{directory}}` 

- Check if your linux system is a 32- or 64-bit system

`getconf LONG_BIT`

- Check how many processes a user can run at once

`getconf CHILD_MAX`

- List every configuration value and then find patterns with the grep command. i.e every value with MAX in it.

`getconf -a | grep MAX`
