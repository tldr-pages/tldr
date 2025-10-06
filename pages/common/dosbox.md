# dosbox

> MS-DOS emulator to run legacy DOS applications and games.
> More information: <https://www.dosbox.com/wiki/Usage>.

- Start DOSBox with default settings:

`dosbox`

- Run a DOS executable located at a specific path:

`dosbox {{path/to/executable.exe}}`

- Mount a folder as C: and run an executable:

`dosbox {{path/to/executable.exe}} -c "MOUNT C {{path/to/folder}}"`

- Start DOSBox in fullscreen mode:

`dosbox -fullscreen`

- Exit DOSBox automatically after running a program:

`dosbox {{path/to/executable.exe}} -exit`
