# vboxmanage-controlvm

> Change the state and the settings of a currently running virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>.

- Temporarily stop the execution of a virtual machine:

`VBoxManage controlvm {{uuid|vm_name}} pause`

- Resume the execution of a paused virtual machine:

`VBoxManage controlvm {{uuid|vm_name}} resume`

- Perform a cold reset on the virtual machine:

`VBoxManage controlvm {{uuid|vm_name}} reset`

- Poweroff a virtual machine with the same effect as pulling the power cable of a computer:

`VBoxManage controlvm {{uuid|vm_name}} poweroff`

- Shutdown the virtual machine and save its current state:

`VBoxManage controlvm {{uuid|vm_name}} savestate`

- Send an ACPI (Advanced Configuration and Power Interface) shutdown signal to the virtual machine:

`VBoxManage controlvm {{uuid|vm_name}} acpipowerbutton`

- Send command to reboot itself to the guest OS:

`VBoxManage controlvm {{uuid|vm_name}} reboot`

- Shutdown down the virtual machine without saving its state:

`VBoxManage controlvm {{uuid|vm_name}} shutdown`
