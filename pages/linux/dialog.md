# dialog

> Display dialog boxes on the terminal.
> See also: `gum`, `whiptail`.
> More information: <https://manned.org/dialog>.

- Display a message:

`dialog --msgbox "{{Message}}" {{height}} {{width}}`

- Prompt the user for text:

`dialog --inputbox "{{Enter text:}}" {{8}} {{40}} 2>{{output.txt}}`

- Prompt the user for a yes/no question:

`dialog --yesno "{{Continue?}}" {{7}} {{40}}`

- Display help:

`dialog`
