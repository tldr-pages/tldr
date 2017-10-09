# stat

> Display file and filesystem information.

- Show file properties such as size, permissions, creation and access dates among others:

`stat {{file}}`

- Same as a above but in a more concise way:

`stat -t {{file}}`

- Display filesystem information:

`stat -f {{file}}`

- Use stat to show only octal file permissions:

`stat -c "%a %n" {{file}}`

- Show octal file permissions, name and group of the file owner:

`stat -c "%a %n %U %G" {{file}}`

- Show the size in bytes of the file:

`stat -c "%s %n" {{file}}`
