# gio trash

> Package to manager trash bin.
> Library glib used by gnome to handle trash.
> More information: <https://gitlab.gnome.org/GNOME/glib>.

- Add to trash:

`gio trash {{path/to/file/or/folder}}`

- List itens in trash:

`gio trash --list`

- Restore from trash using id:

`gio trash trash:///{{id}}`
