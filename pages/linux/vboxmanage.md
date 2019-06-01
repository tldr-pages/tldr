# VBoxManage

> VBoxManage is the command-line interface to VirtualBox.
> With it, you can completely control VirtualBox from the command line.
> Homepage: <https://www.virtualbox.org>.

- List all Virtualbox virtual machines:

`VBoxManage list vms`

- Show information about a particular virtual machine:

`VBoxManage showvminfo {{name|uuid}}`

- Start a virtual machine:

`VBoxManage startvm {{name|uuid}}`

- Start a virtual machine in headless mode:

`VBoxManage startvm {{name|uuid}} -type headless`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm {{name|uuid}} savestate`

- Shutdown down the virtual machine without saving state:

`VBoxManage controlvm {{name|uuid}} poweroff`
