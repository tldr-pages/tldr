# gnome-screenshot

> Capture the screen, a window, or a user-defined area and save the image to a file.
> More information: <https://apps.gnome.org/app/org.gnome.Screenshot>.

- Take a screenshot and save it to the default location, normally `~/Pictures`:

`gnome-screenshot`

- Take a screenshot and save it to the named file location:

`gnome-screenshot --file {{path/to/file}}`

- Take a screenshot and save it to the clipboard:

`gnome-screenshot --clipboard`

- Take a screenshot after the specified number of seconds:

`gnome-screenshot --delay {{5}}`

- Launch the GNOME Screenshot GUI:

`gnome-screenshot --interactive`

- Take a screenshot of the current window and save it to the specified file location:

`gnome-screenshot --window --file {{path/to/file}}`

- Take a screenshot after the specified number of seconds and save it to the clipboard:

`gnome-screenshot --delay {{10}} --clipboard`

- Display the version:

`gnome-screenshot --version`
