# xdg-settings

> Manage settings of XDG-compatible desktop environments.
> More information: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- Print the default web browser:

`xdg-settings get {{default-web-browser}}`

- Set the default web browser to Firefox:

`xdg-settings set {{default-web-browser}} {{firefox.desktop}}`

- Set the default mail URL scheme handler to Evolution:

`xdg-settings set {{default-url-scheme-handler}} {{mailto}} {{evolution.desktop}}`

- Set the default PDF document viewer:

`xdg-settings set {{pdf-viewer.desktop}}`

- Display help:

`xdg-settings --help`
