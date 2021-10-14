# wsl-open

> Open a file or URL from within the Windows Subsystem for Linux command line in user's preferred Windows GUI applications.
> More information: <https://gitlab.com/4U6U57/wsl-open>.

- Open the current directory in Windows Explorer:

`wsl-open .`

- Open a URL in the default Windows browser:

`wsl-open {{https://example.com}}`

- Open an image in the default Windows image viewer:

`wsl-open {{path/to/image.png}}`

- Associate wsl-open with links (set wsl-open as your shell's BROWSER):

`wsl-open -w`

- Display help:

`wsl-open -help`
