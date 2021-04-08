# apt-file

> Search for files in apt packages, including ones not yet installed.
> More information: <https://manned.org/apt-file.1>.

- Update the metadata database:

`sudo apt update`

- Search for packages that contain the specified file or path:

`apt-file {search|find} {{part/of/filename}}`

- List the contents of a specific package:

`apt-file {show|list} {{package_name}}`

- Search for packages that match the regular expresssion given in `pattern`:

`apt-file {search|find} --regexp {{pattern}}`
