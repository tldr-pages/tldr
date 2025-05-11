# apt-file

> Search for files in `apt` packages, including ones not yet installed.
> More information: <https://manned.org/apt-file.1>.

- Update the metadata database:

`sudo apt update`

- Search for packages that contain the specified file or path:

`apt-file {{search|find}} {{partial_path/to/file}}`

- List the contents of a specific package:

`apt-file {{show|list}} {{package}}`

- Search for packages that match the `regular_expression`:

`apt-file {{search|find}} {{[-x|--regexp]}} {{regular_expression}}`
