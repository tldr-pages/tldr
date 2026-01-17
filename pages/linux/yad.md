# yad

> Display GTK+ dialogs from shell scripts.
> See also: `zenity`.
> More information: <https://manned.org/yad>.

- Display a text information dialog:

`yad --text-info --filename={{path/to/file.txt}}`

- Open a text entry dialog and return the input to `stdout`:

`yad --entry --text "{{message}}"`

- Select a file:

`yad --file --title={{Select a file}}`

- Select a date from a calendar:

`yad --calendar --title={{Select a date}}`

- Display a list:

`yad --list --column={{Name}} --column={{Age}} {{Alice}} {{20}} {{Bob}} {{30}}`

- Open a pulsating progress bar that automatically closes at 100%:

`{{command}} | yad --progress --pulsate --auto-close --text "{{message}}"`
