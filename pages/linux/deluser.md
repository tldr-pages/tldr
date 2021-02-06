# deluser

> Delete user from system
> All commands must be executed as root (`sudo [command]`)

- Remove a user:

`deluser {{name}}`

- Remove a user and their home directory:

`deluser --remove-home {{name}}`

- Remove a user and their home, but backup it's files first:

`deluser --backup-to {{path/to/backup}} --remove-home {{name}}`

- Remove a user, and all files owned by them:

`deluser --remove-all-files {{name}}
