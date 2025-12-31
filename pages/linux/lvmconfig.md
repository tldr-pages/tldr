# lvmconfig

> Display and manipulate LVM configuration information.
> More information: <https://manned.org/lvmconfig>.

- Display the effective configuration in use (after merging all config sources):

`lvmconfig --typeconfig current --mergedconfig`

- Show only settings that differ from their defaults:

`lvmconfig --typeconfig diff`

- List all configuration keys:

`lvmconfig {{[-l|--list]}}`

- Print the default configuration with full comments and extra spacing:

`lvmconfig --typeconfig default --withcomments --withspaces`

- Validate the full merged configuration and report errors:

`lvmconfig --mergedconfig --validate`

- Write the current effective configuration to a file:

`lvmconfig --typeconfig current {{[-f|--file]}} {{path/to/output.conf}}`
