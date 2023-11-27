# vboxmanage-unregistervm

> Unregister a virtual machine (VM).
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>.

- Unregister an existing VM:

`VBoxManage unregistervm {{uuid|vm_name}}`

- Delete hard disk image files, all saved state files, VM logs, XML VM machine files:

`VBoxManage unregistervm {{uuid|vm_name}} --delete`

- Delete all files from the VM:

`VBoxManage unregistervm {{uuid|vm_name}} --delete-all`
