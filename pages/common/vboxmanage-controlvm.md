# vboxmanage-controlvm

> Change the state and the settings of a currently running virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>.

- Temporary stops the execution of a virtual machine:

`VBoxManage controlvm {{uuid|vmname}}  pause`

- Resume the execution of a paused virtual machine:

`VBoxManage controlvm {{uuid|vmname}} resume`

- Perform a cold reset on the virtual machine:

`VBoxManage controlvm {{uuid|vmname}} reset`

- Poweroff a virtual machine with the same effect as pulling the power cable of a computer:

`VBoxManage controlvm {{uuid|vmname}} poweroff`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm {{uuid|vmname}} savestate`

- Send an ACPI shutdown signal to the virtual machine:

`VBoxManage controlvm {{uuid|vmname}} acpipowerbutton`

- Send command to reboot itself to the guest OS:

`VBoxManage controlvm {{uuid|vmname}} reboot`

- Shutdown down the virtual machine without saving its state:

`VBoxManage controlvm {{uuid|vmname}} shutdown`
