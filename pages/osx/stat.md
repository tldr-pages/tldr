# stat

> Display file status.

- Show file properties such as size, permissions, creation and access dates among others:

`stat {{file}}`

- Same as a but verbose (more similar to linux's `stat`:

`stat -x {{file}}`

- Use stat to show only octal file permissions:

`stat -f %Mp%Lp {{file}}`

- Show octal file permissions, name and group of the file owner:

`stat -f "%Mp%Lp %N %Su %Sg" {{file}}`

- Show the size in bytes of the file:

`stat -f "%z %N" {{file}}`
