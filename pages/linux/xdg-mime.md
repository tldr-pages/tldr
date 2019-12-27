# xdg-mime

> Query and change desktop file type handling.
> More information: <https://www.freedesktop.org/wiki/Software/xdg-utils/>.

- View default application for opening filetype:

`xdg-mime query default {{filetype}}`

- Change default application for opening filetype:

`xdg-mime default {{application}}.desktop {{filetype}}`

- Find out the filetype of a url or path:

`xdg-mime query filetype {{path/to/file}}`
