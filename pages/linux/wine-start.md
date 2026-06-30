# wine start

> Launch a program or open a document in a Wine prefix.
> A reimplementation of the Windows `start` command.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Launch a Windows program:

`wine start {{path\to\program.exe}}`

- Open a document with its associated program:

`wine start {{path\to\document.ext}}`

- Launch a program from a Unix-style path:

`wine start /unix {{path/to/program.exe}}`

- Launch a program and wait for it to exit, returning its exit code:

`wine start /wait {{path\to\program.exe}}`

- Launch a program minimized or maximized:

`wine start {{/min|/max}} {{path\to\program.exe}}`

- Launch a program from a specific working directory:

`wine start /d {{path\to\directory}} {{path\to\program.exe}}`

- Launch a program without opening a new console window:

`wine start /b {{path\to\program.exe}}`

- Display help:

`wine start /?`
