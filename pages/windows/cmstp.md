# cmstp

> A command-line tool for managing connection service profiles.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Install the specified profile:

`cmstp {{path/to/profile}}`

- Uninstall the specified profile:

`cmstp /u {{path/to/profile}}`

- Install the specified profile [s]ilently without any prompts:

`cmstp /s {{path/to/profile}}`

- Install the specified profile without checking for dependencies:

`cmstp /nf {{path/to/profile}}`

- Install the specified profile for the current user:

`cmstp /su {{path/to/profile}}`

- Install the specified profile for [a]ll [u]sers (requires administrator privileges):

`cmstp /au {{path/to/profile}}`
