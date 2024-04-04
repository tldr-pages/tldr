# doas

> Executes a command as another user.
> More information: <https://man.openbsd.org/doas>.

- Run a command as root:

`doas {{command}}`

- Run a command as another user:

`doas -u {{user}} {{command}}`

- Launch the default shell as root:

`doas -s`

- Parse a configuration file and check if the execution of a command as another user is allowed:

`doas -C {{config_file}} {{command}}`

- Make `doas` request a password even after it was supplied earlier:

`doas -L`
