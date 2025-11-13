# localectl

> Control the system locale and keyboard layout settings.
> More information: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- Show the current settings of the system locale and keyboard mapping:

`localectl`

- List available locales:

`localectl list-locales`

- Set a system locale variable:

`sudo localectl set-locale {{LANG}}={{en_US.UTF-8}}`

- List available keymaps:

`localectl list-keymaps`

- Set the system keyboard mapping for the console and X11:

`sudo localectl set-keymap {{us}}`
