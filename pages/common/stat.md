# stat

> Display file and filesystem information.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Display properties about a specific file such as size, permissions, creation and access dates among others:

`stat {{path/to/file}}`

- Display properties about a specific file such as size, permissions, creation and access dates among others without labels:

`stat {{[-t|--terse]}} {{path/to/file}}`

- Display information about the filesystem where a specific file is located:

`stat {{[-f|--file-system]}} {{path/to/file}}`

- Show only octal file permissions:

`stat {{[-c|--format]}} "%a %n" {{path/to/file}}`

- Show the owner and group of a specific file:

`stat {{[-c|--format]}} "%U %G" {{path/to/file}}`

- Show the size of a specific file in bytes:

`stat {{[-c|--format]}} "%s %n" {{path/to/file}}`
