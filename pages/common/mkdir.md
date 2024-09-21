# mkdir

> Create directories and set their permissions.
> More information: <https://www.gnu.org/software/coreutils/mkdir>.

- Create specific directories:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Create specific directories and their parents if needed:

`mkdir {{-p|--parents}} {{path/to/directory1 path/to/directory2 ...}}`

- Create directories with specific permissions:

`mkdir {{-m|--mode}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`
