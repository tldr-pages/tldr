# cmstp

> Manage connection service profiles.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Install a specific profile:

`cmstp "{{path\to\profile_file}}"`

- Install without creating a desktop shortcut:

`cmstp /ns "{{path\to\profile_file}}"`

- Install without checking for dependencies:

`cmstp /nf "{{path\to\profile_file}}"`

- Only install for the current user:

`cmstp /su "{{path\to\profile_file}}"`

- Install for all users (requires administrator privileges):

`cmstp /au "{{path\to\profile_file}}"`

- Install silently without any prompts:

`cmstp /s "{{path\to\profile_file}}"`

- Uninstall a specific profile:

`cmstp /u "{{path\to\profile_file}}"`

- Uninstall silently without a confirmation prompt:

`cmstp /u /s "{{path\to\profile_file}}"`
