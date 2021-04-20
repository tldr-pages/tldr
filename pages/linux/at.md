# at

> Executes commands at a specified time.
> More information: <https://man.archlinux.org/man/at.1>.

- Open an `at` prompt to create a new set of scheduled commands, press `Ctrl + D` to save and exit:

`at {{hh:mm}}`

- Execute the commands and email the result using a local mailing program such as sendmail:

`at {{hh:mm}} -m`

- Execute a script at the given time:

`at {{hh:mm}} -f {{path/to/file}}`

- Display a system notification at 11pm on February 18th:

`echo "notify-send '{{Wake up!}}'" | at {{11pm}} {{Feb 18}}`
