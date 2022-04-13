# mkdir

> Creates directories and sets their permissions.
> More information: <https://www.gnu.org/software/coreutils/mkdir>.

- Create specific directories:

`mkdir {{path/to/directory{1,2,...}}}`

- Create specific nested directories recursively:

`mkdir --parents {{path/to/directory{1,2,...}}}`

- Create directories with specific permissions:

`mkdir --mode={{rwxrw-r--}} {{path/to/directory{1,2,...}}}`
