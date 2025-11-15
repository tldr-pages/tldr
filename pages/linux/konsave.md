# konsave

> Save and apply your Linux customizations with just one command.
> More information: <https://github.com/Prayag2/konsave>.

- Save the current configuration as a profile:

`konsave {{[-s|--save]}} {{profile_name}}`

- Apply a profile:

`konsave {{[-a|--apply]}} {{profile_name}}`

- Save the current configuration as a profile, overwriting existing profiles if they exist with the same name:

`konsave {{[-s|--save]}} {{profile_name}} {{[-f|--force]}}`

- List all profiles:

`konsave {{[-l|--list]}}`

- Remove a profile:

`konsave {{[-r|--remove]}} {{profile_name}}`

- Export a profile as a `.knsv` to the home directory:

`konsave {{[-e|--export-profile]}} {{profile_name}}`

- Import a `.knsv` profile:

`konsave {{[-i|--import-profile]}} {{path/to/profile_name.knsv}}`
