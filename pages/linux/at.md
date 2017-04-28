# at

> Executes commands at a specified time.

- Open an `at` prompt to create a new set of scheduled commands, press `Ctrl + D` to save and exit:

`at {{hh:mm:ss}}`

- Execute the commands and email the result using a local mailing program such as sendmail:

`at {{hh:mm:ss}} -m`

- Execute a script at the given time:

`at {{hh:mm:ss}} -f {{path/to/file}}`
