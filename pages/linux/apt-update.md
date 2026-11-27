# apt update

> Download package information from configured sources for Debian-based distributions.
> More information: <https://manned.org/apt.8>.

- Update the list of available packages and versions:

`sudo apt update`

- Update package lists in quiet mode, suppressing progress output:

`sudo apt update {{[-q|--quiet]}}`

- Update package lists using a specific configuration file:

`sudo apt update {{[-c|--config-file]}} {{path/to/file.conf}}`

- Display the URIs of the package lists without downloading them:

`apt update --print-uris`
