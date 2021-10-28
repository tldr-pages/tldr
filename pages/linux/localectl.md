# localectl

> Control the system locale and keyboard layout settings.
> More information: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- Show current settings of the system locale and keyboard mapping:

`localectl`

- List available locales:

`localectl list-locales`

- Set a system locale variable:

`localectl set-locale {{LANG}}={{en_US.UTF-8}}`

- Set the system keyboard mapping for the console and X11:

`localectl set-keymap {{en}}`
