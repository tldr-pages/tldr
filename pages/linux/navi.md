# navi

> An interactive cheatsheet tool for the command line and application launchers.
> More information: <https://github.com/denisidoro/navi>.

- Browse through all available cheatsheets:

`navi`

- Browse the cheatsheet for `navi` itself:

`navi fn welcome`

- Print a command from the cheatsheet without executing it:

`navi --print`

- Output shell widget source code (It automatically detects your shell if possible, but can also be specified manually):

`navi widget {{shell}}`

- Autoselect and execute the snippet that best matches a query:

`navi --query '{{query}}' --best-match`
