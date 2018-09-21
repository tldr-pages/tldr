# cmd

> The Windows command interpreter.

- Start a new instance of the command interpreter:

`cmd`

- Run the specified command and terminate:

`cmd /c "{{command}}"`

- Run the specified command without terminating:

`cmd /k "{{command}}"`

- Disable the usage of `echo` in command output:

`cmd /q`

- Enable or disable command extensions:

`cmd /e:{{on|off}}`

- Enable or disable file or directory autocompletion:

`cmd /f:{{on|off}}`

- Enable or disable environment variable expansion:

`cmd /v:{{on|off}}`

- Force output to use unicode encoding:

`cmd /u`
