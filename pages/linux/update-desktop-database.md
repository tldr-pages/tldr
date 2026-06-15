# update-desktop-database

> Build the cache database of MIME types handled by desktop files.
> More information: <https://manned.org/update-desktop-database>.

- Update the desktop file MIME type cache for standard system directories:

`sudo update-desktop-database`

- Update the cache for a specific desktop file directory:

`update-desktop-database {{path/to/directory}}`

- Update the cache for multiple directories:

`update-desktop-database {{path/to/directory1 path/to/directory2 ...}}`

- Update the cache without displaying any output:

`update-desktop-database {{[-q|--quiet]}}`

- Update the cache with verbose output:

`update-desktop-database {{[-v|--verbose]}}`
