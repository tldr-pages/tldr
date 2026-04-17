# eselect

> A system administration and configuration tool for Gentoo Linux.
> Some subcommands such as `profile` have their own usage documentation.
> More information: <https://wiki.gentoo.org/wiki/Eselect>.

- List all available system profiles:

`eselect profile list`

- Set a system profile by its index or name:

`eselect profile set {{index|name}}`

- List available versions of a specific tool (e.g., Python):

`eselect {{python}} list`

- Set the active version of a specific tool:

`eselect {{python}} set {{index|name}}`

- List available kernel symlinks:

`eselect kernel list`

- Create a symlink to a specific kernel directory:

`eselect kernel set {{index|name}}`

- Display help for a specific module:

`eselect help {{module_name}}`
