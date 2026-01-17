# zenity

> Display dialogs from the command-line/shell scripts.
> Return user-inserted values or 1 if error.
> More information: <https://manned.org/zenity>.

- Display the default question dialog:

`zenity --question`

- Display an info dialog displaying a message:

`zenity --info --text "{{message}}"`

- Display a name/password form and output the data separated by ";" ("|" by default):

`zenity --forms --add-entry "{{name_label}}" --add-password "{{password_label}}" --separator ";"`

- Display a file selection form in which the user can only select directories:

`zenity --file-selection --directory`

- Display a progress bar which updates its message every second and show a progress percent:

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`
