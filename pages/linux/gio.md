# gio

> Handle local and virtual files (GVfs).
> Part of GLib used in GNOME-based systems.
> More information: <https://manned.org/gio>.

- Open a file with the default application (e.g. PDF, image):

`gio open {{path/to/file}}`

- List files in a directory:

`gio list {{path/to/directory}}`

- Show information about a file:

`gio info {{path/to/file}}`

- Copy a file:

`gio copy {{path/to/source}} {{path/to/destination}}`

- Send a file to the trash (reversible):

`gio trash {{path/to/file}}`
