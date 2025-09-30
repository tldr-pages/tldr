# gksudo

> Frontend for `sudo`.
> Allows you to run graphical commands which need root access without having to run an X terminal emulator.
> Note: This command is deprecated in favor of commands like `pkexec`, and is no longer maintained.
> See also: `gksu`.
> More information: <https://manned.org/man/gksudo>.

- Run a command as a specific user:

`gksudo {{[-u|--user]}} {{userid}} {{command}}`

- Run the command while preserving the current environments:

`gksudo {{[-u|--user]}} {{userid}} {{[-k|--preserve-env]}} {{command}}`

- Force `gksudo` to use `su` to run the command:

`gksu {{[-u|--user]}} {{userid}} {{[-w|--su-mode]}} {{command}}`

- Force `gksudo` to use `sudo` to run the command:

`gksudo {{[-u|--user]}} {{userid}} {{[-S|--sudo-mode]}} {{command}}`

- Output debug info for the given command:

`gksudo {{[-u|--user]}} {{userid}} {{[-d|--debug]}} {{command}}`
