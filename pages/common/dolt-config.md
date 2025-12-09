# dolt config

> Read and write local (per repository) and global (per user) Dolt configuration variables.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-config>.

- List all local and global configuration options and their values:

`dolt config --list`

- Display the value of a local or global configuration variable:

`dolt config --get {{name}}`

- Modify the value of a local configuration variable, creating it if it doesn't exist:

`dolt config --add {{name}} {{value}}`

- Modify the value of a global configuration variable, creating it if it doesn't exist:

`dolt config --global --add {{name}} {{value}}`

- Delete a local configuration variable:

`dolt config --unset {{name}}`

- Delete a global configuration variable:

`dolt config --global --unset {{name}}`
