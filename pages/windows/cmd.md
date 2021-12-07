# cmd

> The Windows command interpreter.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start an interactive shell session:

`cmd`

- Execute a [c]ommand:

`cmd /c "{{command}}"`

- Execute a script:

`cmd {{path/to/file.bat}}`

- Execute a command and then enter an interactive shell:

`cmd /k "{{command}}"`

- Start an interactive shell session where `echo` is disabled in command output:

`cmd /q`

- Start an interactive shell session with delayed [v]ariable expansion enabled or disabled:

`cmd /v:{{on|off}}`

- Start an interactive shell session with command [e]xtensions enabled or disabled:

`cmd /e:{{on|off}}`

- Start an interactive shell session with used Unicode encoding:

`cmd /u`
