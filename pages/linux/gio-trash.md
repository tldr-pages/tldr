# gio trash

> Move files to the trash bin.
> Used by `gnome` to handle trash.
> More information: <https://gitlab.gnome.org/GNOME/glib>.

- Add specific files to trash:

`gio trash {{path/to/file_or_folder1 path/to/file_or_folder2 ...}}`

- List items in trash:

`gio trash --list`

- Restore from trash using id:

`gio trash trash:///{{id}}`
