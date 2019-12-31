# VBoxManage

> Command-line interface to VirtualBox.
> Includes all the functionality of the GUI and more.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>.

- List all VirtualBox virtual machines:

`VBoxManage list vms`

- Show information about a particular virtual machine:

`VBoxManage showvminfo {{name|uuid}}`

- Start a virtual machine:

`VBoxManage startvm {{name|uuid}}`

- Start a virtual machine in headless mode:

`VBoxManage startvm {{name|uuid}} -type headless`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm {{name|uuid}} savestate`

- Shutdown down the virtual machine without saving its state:

`VBoxManage controlvm {{name|uuid}} poweroff`
