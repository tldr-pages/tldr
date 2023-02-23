# virtualboxvm

> The VirtualBox virtual machine management CLI.
> More information: <https://www.virtualbox.org>.

- Start a virtual machine:

`virtualboxvm --startvm {{name|uuid}}`

- Start a virtual machine in fullscreen mode:

`virtualboxvm --startvm {{name|uuid}} --fullscreen`

- Mount the specified DVD image file:

`virtualboxvm --startvm {{name|uuid}} --dvd {{path\to\image_file}}`

- Display a command-line window with debug information:

`virtualboxvm --startvm {{name|uuid}} --debug-command-line`

- Start a virtual machine in a paused state:

`virtualboxvm --startvm {{name|uuid}} --start-paused`
