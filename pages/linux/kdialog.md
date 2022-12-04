# kdialog

> Show KDE dialog boxes from within shell scripts.
> More information: <https://develop.kde.org/deploy/kdialog/>.

- Open a dialog box displaying a specific message:

`kdialog --msgbox "{{message}}" "{{optional_detailed_message}}"`

- Open a question dialog with a `yes` and `no` button, returning `0` and `1`, respectively:

`kdialog --yesno "{{message}}"`

- Open a warning dialog with a `yes`, `no`, and `cancel` button, returning `0`, `1`, or `2` respectively:

`kdialog --warningyesnocancel "{{message}}"`

- Open an input dialog box and print the input to `stdout` when `OK` is pressed:

`kdialog --inputbox "{{message}}" "{{optional_default_text}}"`

- Open a dialog to prompt for a specific password and print it to `stdout`:

`kdialog --password "{{message}}"`

- Open a dialog containing a specific dropdown menu and print the selected item to `stdout`:

`kdialog --combobx "{{message}}" "{{item1}}" "{{item2}}" "{{...}}"`

- Open a file chooser dialog and print the selected file's path to `stdout`:

`kdialog --getopenfilename`

- Open a progressbar dialog and print a DBUS reference for communication to `stdout`:

`kdialog --progressbar "{{message}}"`
