# apt-file

> Search for files in `apt` packages, including ones not yet installed.
> More information: <https://manned.org/apt-file>.

- Update the metadata database:

`sudo apt update`

- Search for packages that contain the specified file or path:

`apt-file search {{path/to/file}}`

- List the contents of a specific package:

`apt-file list {{package}}`

- Search for packages that match the `regex`:

`apt-file search {{[-x|--regexp]}} {{regex}}`
