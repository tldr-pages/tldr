# konsave

> Save and apply your Linux customizations with just one command.
> More information: <https://github.com/Prayag2/konsave>.

- Save the current configuration as a profile:

`konsave --save {{profile_name}}`

- Apply a profile:

`konsave --apply {{profile_name}}`

- Save the current configuration as a profile, overwriting existing profiles if they exist with the same name:

`konsave -s {{profile_name}} --force`

- List all profiles:

`konsave --list`

- Remove a profile:

`konsave --remove {{profile_name}}`

- Export a profile as a `.knsv` to the home directory:

`konsave --export-profile {{profile_name}}`

- Import a `.knsv` profile:

`konsave --import-profile {{path/to/profile_name.knsv}}`
