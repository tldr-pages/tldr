# konsole

> KDE's terminal emulator.
> More information: <https://docs.kde.org/trunk5/en/konsole/konsole/command-line-options.html>.

- Open the terminal in a specific directory:

`konsole --workdir {{path/to/directory}}`

- [e]xecute a specific command and don't close the window after it exits:

`konsole --noclose -e "{{command}}"`

- Open a new tab:

`konsole --new-tab`

- Open the terminal in the background and bring to the front when `Ctrl+Shift+F12` is pressed:

`konsole --background-mode`
