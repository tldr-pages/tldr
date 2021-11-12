# cmd

> The Windows command interpreter.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start an interactive shell session:

`cmd`

- Execute a [c]ommand:

`cmd /c "{{command}}"`

- Execute a command and then enter an interactive shell:

`cmd /k "{{command}}"`

- Start an interactive shell session with disabled usage of `echo` in command output:

`cmd /q`

- Start an interactive shell session with enabled or disabled command [e]xtensions:

`cmd /e:{{on|off}}`

- Execute a script:

`cmd "{{path/to/file.bat}}"`
