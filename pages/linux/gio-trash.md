# gio trash

> Move files to the trash bin.
> Used by GNOME to handle trash.
> More information: <https://gitlab.gnome.org/GNOME/glib>.

- Move specific files to trash:

`gio trash {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List items in trash:

`gio trash --list`

- Restore a specific item from trash using its ID:

`gio trash trash:///{{id}}`
