# vboxmanage-registervm

> Register a virtual machine (VM).
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>.

- Register an existing VM:

`VBoxManage registervm {{path/to/filename.vbox}}`

- Supply the encryption password file of the VM:

`VBoxManage registervm {{path/to/filename.vbox}} --password {{path/to/password_file}}`

- Prompt for the encryption password on the command line:

`VBoxManage registervm {{path/to/filename.vbox}} --password -`
