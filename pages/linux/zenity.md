# zenity

> Display dialogs from the command line/shell scripts, and return user-inserted values or 1 if error.

- Display the default question dialog:

`zenity --quesion`

- Display an info dialog displaying the text "Hello!":

`zenity --info --text="Hello!"`

- Display a name/password form and output the data separated by ';':

`zenity --forms --add-entry="Name" --add-password="Password" --separator=";"`

- Display a file selection form where the user can only select directories:

`zenity --file-selection --directory`

- Display a progress bar and update it:

`(echo "# First task"; sleep 2s; echo "50"; echo "# Second task"; sleep 2s; echo "100") | zenity --progress`
