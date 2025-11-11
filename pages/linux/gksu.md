# gksu

> Frontend for `su`.
> Allows you to run graphical commands which need root access without having to run an X terminal emulator.
> Note: This command is deprecated in favor of commands like `pkexec`, and is no longer maintained.
> See also: `gksudo`.
> More information: <https://manned.org/gksudo>.

- Run a command as a specific user:

`gksu {{[-u|--user]}} {{userid}} {{command}}`

- Run the command while preserving the current environments:

`gksu {{[-u|--user]}} {{userid}} {{[-k|--preserve-env]}} {{command}}`

- Force `gksu` to use `su` to run the command:

`gksu {{[-u|--user]}} {{userid}} {{[-w|--su-mode]}} {{command}}`

- Force `gksu` to use `sudo` to run the command:

`gksu {{[-u|--user]}} {{userid}} {{[-S|--sudo-mode]}} {{command}}`

- Output debug info for the given command:

`gksu {{[-u|--user]}} {{userid}} {{[-d|--debug]}} {{command}}`
