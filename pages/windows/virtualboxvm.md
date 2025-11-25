# virtualboxvm

> VirtualBox VM launcher (Windows) — deprecated or non-standard.
> More information: <https://www.virtualbox.org/manual/ch08.html>.

- Start a VM by name or UUID:

`virtualboxvm --startvm {{name|uuid}}`

- Start in fullscreen:

`virtualboxvm --startvm {{name|uuid}} --fullscreen`

- Mount a DVD image:

`virtualboxvm --startvm {{name|uuid}} --dvd {{path\to\image_file}}`

- Debug with command-line window:

`virtualboxvm --startvm {{name|uuid}} --debug-command-line`

- Start a VM in a paused state:

`virtualboxvm --startvm {{name|uuid}} --start-paused`

- List VMs (use VBoxManage instead):

`VBoxManage list vms`

- Start a VM using VBoxManage:

`VBoxManage startvm {{name|uuid}}`
