# stat

> Display file and filesystem information.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Show a specific file properties such as size, permissions, creation and access dates among others:

`stat {{path/to/file}}`

- Same as above but in a more concise way:

`stat -t {{path/to/file}}`

- Show a filesystem information:

`stat -f {{path/to/file}}`

- Show only octal file permissions:

`stat -c "%a %n" {{path/to/file}}`

- Show an owner and a group of a specific file:

`stat -c "%U %G" {{path/to/file}}`

- Show a size of a specific file in bytes:

`stat -c "%s %n" {{path/to/file}}`
