# yad

> Display GTK+ dialogs from shell scripts.
> See also: `zenity`.
> More information: <https://manned.org/yad>.

- Display the contents of a file in a text information dialog:

`yad --text-info --filename {{path/to/file}}`

- Open a text entry dialog and return the input to `stdout`:

`yad --entry --text "{{message}}"`

- Open a file picker with a specific title:

`yad --file --title "{{title_message}}"`

- Open a date picker dialog with a specific title:

`yad --calendar --title "{{title_message}}"`

- Display a list dialog with multiple columns and data:

`yad --list --column "{{col1}}" --column "{{col2}}" {{col1_row1 col2_row1 col1_row2 col2_row2 ...}}`

- Open a pulsating progress bar that automatically closes at 100%:

`{{command}} | yad --progress --pulsate --auto-close --text "{{message}}"`
