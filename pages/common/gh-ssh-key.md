# gh ssh-key

> Manage GitHub SSH keys from the command line.
> More information: <https://cli.github.com/manual/gh_ssh-key>.

- Display help:

`gh ssh-key`

- List SSH keys:

`gh ssh-key list`

- Add an SSH key to the user:

`gh ssh-key add {{path/to/key.pub}}`

- Add an SSH key to the user with a specific title:

`gh ssh-key add --title {{title}} {{path/to/key.pub}}`
