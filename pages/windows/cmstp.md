# cmstp

> A command-line tool for managing connection service profiles.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Install a specific profile:

`cmstp "{{path/to/profile}}"`

- Install without creating a desktop shortcut:

`cmstp /ns "{{path/to/profile}}"`

- Install without checking for dependencies:

`cmstp /nf "{{path/to/profile}}"`

- Only install for the current user:

`cmstp /su "{{path/to/profile}}"`

- Install for all users (requires administrator privileges):

`cmstp /au "{{path/to/profile}}"`

- Install silently without any prompts:

`cmstp /s "{{path/to/profile}}"`

- Uninstall a specific profile:

`cmstp /u "{{path/to/profile}}"`

- Uninstall silently without a confirmation prompt:

`cmstp /u /s "{{path/to/profile}}"`
