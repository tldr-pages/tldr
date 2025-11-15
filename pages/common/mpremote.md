# mpremote

> Remotely control MicroPython devices.
> More information: <https://docs.micropython.org/en/latest/reference/mpremote.html>.

- List all connected MicroPython devices:

`mpremote connect list`

- Open an interactive REPL session with a connected device:

`mpremote connect {{device}}`

- Run a local script on a connected device:

`mpremote run {{path/to/script.py}}`

- Mount a local directory to the device:

`mpremote mount {{path/to/directory}}`

- Install a mip package on the device:

`mpremote mip install {{package}}`
