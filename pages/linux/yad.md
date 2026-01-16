# yad

> Display GTK+ dialogs from shell scripts.
> More information: <https://manned.org/man/yad>.

- Display a text information dialog:

`yad --text-info --filename={{path/to/file.txt}}`

- Prompt for text input:

`yad --entry --text={{Enter your name:}}`

- Select a file:

`yad --file --title={{Select a file}}`

- Select a date from a calendar:

`yad --calendar --title={{Select a date}}`

- Display a list:

`yad --list --column={{Name}} --column={{Age}} {{Alice}} {{20}} {{Bob}} {{30}}`

- Show a progress bar:

`{{command}} | yad --progress --pulsate --auto-close --text={{Working...}}`
