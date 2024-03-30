# apt-file

> Search for files in `apt` packages, including ones not yet installed.
> More information: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Update the metadata database:

`sudo apt update`

- Search for packages that contain the specified file or path:

`apt-file {{search|find}} {{partial_path/to/file}}`

- List the contents of a specific package:

`apt-file {{show|list}} {{package}}`

- Search for packages that match the `regular_expression`:

`apt-file {{search|find}} --regexp {{regular_expression}}`
