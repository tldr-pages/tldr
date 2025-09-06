# chflags

> Change file or directory flags.
> More information: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

- Set the `hidden` flag for a file:

`chflags {{hidden}} {{path/to/file}}`

- Unset the `hidden` flag for a file:

`chflags {{nohidden}} {{path/to/file}}`

- Recursively set the `uchg` flag for a directory:

`chflags -R {{uchg}} {{path/to/directory}}`

- Recursively unset the `uchg` flag for a directory:

`chflags -R {{nouchg}} {{path/to/directory}}`
