# fondue

> A command-line installer for optional Windows features.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- Enable a specific Windows feature:

`fondue /enable-feature:{{feature}}`

- Hide all output messages to the user:

`fondue /enable-feature:{{feature}} /hide-ux:all`

- Specify a caller process name for error reporting:

`fondue /enable-feature:{{feature}} /caller-name:{{name}}`
