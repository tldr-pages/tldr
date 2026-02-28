# apptainer config

> Manage various Apptainer configurations.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_config.html>.

- Add a fakeroot user mapping:

`sudo apptainer config fakeroot {{[-a|--add]}} {{username}}`

- Remove a fakeroot user mapping:

`sudo apptainer config fakeroot {{[-r|--remove]}} {{username}}`

- Enable a fakeroot user mapping:

`sudo apptainer config fakeroot {{[-e|--enable]}} {{username}}`

- Disable a fakeroot user mapping:

`sudo apptainer config fakeroot {{[-d|--disable]}} {{username}}`

- Get the current value of a global configuration directive:

`sudo apptainer config global {{[-g|--get]}} {{directive}}`

- Set a global configuration directive value:

`sudo apptainer config global {{[-s|--set]}} {{directive}} {{value}}`

- Unset a global configuration directive value:

`sudo apptainer config global {{[-u|--unset]}} {{directive}} {{value}}`

- Reset a global configuration directive to its default value:

`sudo apptainer config global {{[-r|--reset]}} {{directive}}`
