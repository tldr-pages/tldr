# gio trash

> Move files to the trash bin.
> Used by GNOME to handle trash.
> More information: <https://manned.org/gio.1>.

- Move specific files to the trash bin:

`gio trash {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List trash bin items:

`gio trash --list`

- Restore a specific item from trash using its ID:

`gio trash trash://{{id}}`
