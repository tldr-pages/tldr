# nu

> Nushell ("a new type of shell") takes a modern, structured approach to your command-line.
> See also: `elvish`.
> More information: <https://www.nushell.sh/book/configuration.html#flag-behavior>.

- Start an interactive shell session:

`nu`

- Execute specific commands:

`nu {{[-c|--commands]}} "{{echo 'nu is executed'}}"`

- Execute a specific script:

`nu {{path/to/script.nu}}`

- Execute a specific script with logging:

`nu --log-level {{error|warn|info|debug|trace}} {{path/to/script.nu}}`
