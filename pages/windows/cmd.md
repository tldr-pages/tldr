# cmd

> The Windows command interpreter.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start an interactive shell session:

`cmd`

- Execute specific [c]ommands:

`cmd /c {{echo Hello world}}`

- Execute a specific script:

`cmd {{path/to/script.bat}}`

- Execute specific commands and then enter an interactive shell:

`cmd /k {{echo Hello world}}`

- Start an interactive shell session where `echo` is disabled in command output:

`cmd /q`

- Start an interactive shell session with delayed [v]ariable expansion enabled or disabled:

`cmd /v:{{on|off}}`

- Start an interactive shell session with command [e]xtensions enabled or disabled:

`cmd /e:{{on|off}}`

- Start an interactive shell session with used [u]nicode encoding:

`cmd /u`
