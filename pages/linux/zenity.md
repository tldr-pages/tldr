# zenity

> Displays dialogs from the command line/shell scripts, and returns user-inserted values or 1 if error.

- Displays the default question dialog:

`zenity --quesion`

- Displays an info dialog displaying the text "Hello!":

`zenity --info --text="Hello!"`

- Display a name/password form and outputs the data separated by ';':

`zenity --forms --add-entry="Name" --add-password="Password" --separator=";"`

- Displays a file selection form where the user can only select directories:

`zenity --file-selection --directory`

- Displays a progress bar and updates it:

`(echo "# First task"; sleep 2s; echo "50"; echo "# Second task"; sleep 2s; echo "100") | zenity --progress
