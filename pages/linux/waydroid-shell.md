# waydroid shell

> Run Android shell commands in Waydroid.
> More information: <https://docs.waydro.id/usage/waydroid-command-line-options>.

- Start an interactive shell in the container:

`sudo waydroid shell`

- Run a command in the container:

`sudo waydroid shell -- {{command}}`

- Start a shell as a specific user ID:

`sudo waydroid shell {{[-u|--uid]}} {{user_id}}`

- List documented Android shell commands:

`tldr {{[-p|--platform]}} android {{[-l|--list]}}`
