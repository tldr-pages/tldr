# gksu

> Frontend for `su`.
> Allows you to run graphical commands which need root access without having to run an X terminal emulator.
> Note: This command is deprecated in favor of commands like `pkexec`, and is no longer maintained.
> See also: `gksudo`.
> More information: <https://manned.org/man/gksudo>.

- Run a command as a specific user:

`gksu {{[-u|--user]}} {{userid}} {{command}}`

- Run the command while preserving the current environments:

`gksu {{[-u|--user]}} {{userid}} {{[--preserve-env|-k]}} {{command}}`

- Force `gksu` to use `su` to run the command:

`gksu {{[-u|--user]}} {{userid}} {{[--su-mode|-w]}} {{command}}`

- Force `gksu` to use `sudo` to run the command:

`gksu {{[-u|--user]}} {{userid}} {{[{{[--sudo-mode|-S]}}]}} {{command}}`

- Output debug info for the given command:

`gksu {{[-u|--user]}} {{userid}} {{[--debug|-d]}} {{command}}`
