# ssh-copy-id

> Use locally available keys to authorise logins on a remote machine

- Copy local key to remote machine

`ssh-copy-id -i {{identity_file}} {{user@hostname}}`

- Copy local key to remote machine which port option

`ssh-copy-id -i {{identity_file}} -p {{port}} {{user@hostname}}`
