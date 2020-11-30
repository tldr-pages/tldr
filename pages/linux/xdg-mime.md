# xdg-mime

> Query and manage MIME types according to the XDG standard.
> More information: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- Display the MIME type of a file:

`xdg-mime query filetype {{path/to/file}}`

- Display the default application for opening PNG images:

`xdg-mime query default {{image/png}}`

- Display the default application for opening a specific file:

`xdg-mime query default $(xdg-mime query filetype {{path/to/file}})`

- Set imv as the default application for opening PNG and JPEG images:

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
