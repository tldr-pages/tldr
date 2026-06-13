# gh ssh-key

> Manage GitHub SSH keys.
> More information: <https://cli.github.com/manual/gh_ssh-key>.

- List SSH keys for the currently authenticated user:

`gh ssh-key {{[ls|list]}}`

- Add an SSH key to the currently authenticated user's account:

`gh ssh-key add {{path/to/key.pub}}`

- Add an SSH key to the currently authenticated user's account with a specific title:

`gh ssh-key add {{[-t|--title]}} {{title}} {{path/to/key.pub}}`

- Display help:

`gh ssh-key`
