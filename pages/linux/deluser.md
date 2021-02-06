# deluser

> Delete user from system.
> Note: all commands must be executed as root.

- Remove a user:

`deluser {{username}}`

- Remove a user and their home directory:

`deluser --remove-home {{username}}`

- Remove a user and their home, but backup it's files first:

`deluser --backup-to {{path/to/backup}} --remove-home {{name}}`

- Remove a user, and all files owned by them:

`deluser --remove-all-files {{username}}`
