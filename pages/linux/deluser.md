# deluser

> Delete a user from the system.
> Note: all commands must be executed as root.
> More information: <https://manpages.debian.org/latest/adduser/deluser.html>.

- Remove a user:

`deluser {{username}}`

- Remove a user and their home directory:

`deluser --remove-home {{username}}`

- Remove a user and their home, but backup their files into a `.tar.gz` file in the specified directory:

`deluser --backup-to {{path/to/backup_directory}} --remove-home {{username}}`

- Remove a user, and all files owned by them:

`deluser --remove-all-files {{username}}`
