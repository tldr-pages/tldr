# nu

> Nushell ("a new type of shell") takes a modern, structured approach to your command-line.
> More information: <https://www.nushell.sh>.

- Start an interactive shell session:

`nu`

- Execute a command and then exit:

`nu --commands "{{command}}"`

- Execute a script:

`nu {{path/to/script.nu}}`

- Execute a script with logging:

`nu --loglevel {{error|warn|info|debug|trace}} {{path/to/script.nu}}`

- Print the Nushell version:

`nu --version`
