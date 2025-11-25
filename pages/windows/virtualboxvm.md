## virtualboxvm

> VirtualBox VM launcher (Windows) — **deprecated or non-standard** in VirtualBox CLI.
> More information: https://www.virtualbox.org/

- Start a VM by name / UUID:  
  `virtualboxvm --startvm {{name|uuid}}`

- Start in fullscreen:  
  `virtualboxvm --startvm {{name|uuid}} --fullscreen`

- Mount a DVD image:  
  `virtualboxvm --startvm {{name|uuid}} --dvd {{path\to\image_file}}`

- Debug with command-line window:  
  `virtualboxvm --startvm {{name|uuid}} --debug-command-line`

- Start a VM in a paused state:  
  `virtualboxvm --startvm {{name|uuid}} --start-paused`

> **Note:** This command is not part of the standard `VBoxManage` CLI. Users are encouraged to use `VBoxManage` for full CLI functionality:
> - List VMs: `VBoxManage list vms` :contentReference[oaicite:4]{index=4}  
> - Start VM: `VBoxManage startvm {{name|uuid}}` :contentReference[oaicite:5]{index=5}  
