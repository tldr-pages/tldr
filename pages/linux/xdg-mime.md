# xdg-mime

> Query and manage MIME types according to the XDG standard.
> More information: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- Find the mime-type of a file:

`xdg-mime query filetype {{path/to/file}}`

- Find the current default application for opening PNG images:

`xdg-mime query default {{image/png}}`

- Set imv as the default application for opening PNG and JPEG images: 

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
