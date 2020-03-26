# doas

> Executes a command as another user

- Run a command as root:

`doas {{command}}`

- Run a command as another user:

`doas -u {{user}} {{command}}`

- Launch the default shell as root:

`doas -s`

- Parse and check a config file to check if the command is permited or denied:

`doas -C {{config_file}} {{command}}`

- Make doas request for a password even after supplied earlier:

`doas -L`
