# wsl-open

> Open a file or URL from within the Windows Subsystem for Linux command line in user's preferred Windows GUI applications.
> More information: <https://gitlab.com/4U6U57/wsl-open>.

- Open the current directory in Windows Explorer:

`wsl-open {{.}}`

- Open a URL in the default web browser in Windows:

`wsl-open {{https://example.com}}`

- Open a specific file in the in the default application in Windows:

`wsl-open {{path/to/file}}`

- Set `wsl-open` as your shell's web browser (open links with `wsl-open`):

`wsl-open -w`

- Display help:

`wsl-open -h`
