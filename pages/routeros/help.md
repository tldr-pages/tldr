# help

> Get the list of possible commands and subdirectories of a given setting directory.
> Equivalent to `ls` in common filesystems.
> Note: For MikroTik RouterOS versions 6.x and below, use `help` or `?` instead of `<F1>`.
> More information: <https://manual.mikrotik.com/docs/management-tools/console>.

- Get list of supported commands and settings subdirectories of the current directory:

`<F1>`

- Get list of supported commands and settings subdirectories of a specific settings directory:

`{{/ip/route}} print`

- Filter out the list by commands and subdirectories starting with a specific query prefix:

`{{/ip/dhcp-}}<Tab>`

- Autocomplete the name of the directory or command (only when there is only 1 filtered result, e.g., `/ip/dhcp-server/`):

`{{/ip/dhcp-s}}<Tab>`

- Print the list in a compact format (useful when `<F1>` is inaccessible using the Terminal console on WebFig):

`<Tab><Tab>`
