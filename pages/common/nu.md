# nu

> Nushell ("a new type of shell") takes a modern, structured approach to your command-line.
> See also: `elvish`.
> More information: <https://www.nushell.sh>.

- Start an interactive shell session:

`nu`

- Execute specific commands:

`nu --commands "{{echo 'nu is executed'}}"`

- Execute a specific script:

`nu {{path/to/script.nu}}`

- Execute a specific script with logging:

`nu --log-level {{error|warn|info|debug|trace}} {{path/to/script.nu}}`
