# fc-cache

> Scan font directories to build font cache files.
> More information: <https://manned.org/fc-cache>.

- Generate font cache files:

`fc-cache`

- Generate font cache files verbosely:

`fc-cache {{[-v|--verbose]}}`

- Force a rebuild of all font cache files, without checking if cache is up-to-date:

`fc-cache {{[-f|--force]}}`

- Erase font cache files, then generate new font cache files:

`fc-cache {{[-r|--really-force]}}`

- Scan a specific directory:

`fc-cache {{path/to/directory}}`

- Scan system-wide directories, skipping the user's home directory:

`fc-cache {{[-s|--system-only]}}`

- Display version:

`fc-cache {{[-V|--version]}}`
