# xdg-settings

> Manage settings of XDG-compatible desktop environments.
> More information: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- Print the default web browser:

`xdg-settings get {{default-web-browser}}`

- Set default web browser to Firefox:

`xdg-settings set default-web-browser firefox.desktop`

- Set default mail URL scheme handler to evolution.desktop:

`xdg-settings set default-url-scheme-handler mailto evolution.desktop`

- Set default PDF document viewer:

`xdg-settings {{pdf-viewer.desktop}}`

- Display help:

`xdg-settings --help`
