# vboxmanage-showvminfo

> Show information about registered virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>.

- Show information about a particular virtual machine:

`VBoxManage showvminfo {{name|uuid}}`

- Show more detailed information about a particular virtual machine:

`VBoxManage showvminfo --details {{name|uuid}}`

- Information is displayed in a machine readable format:

`VBoxManage showvminfo --machinereadable {{name|uuid}}`

- Specify password id if the virtual machine is encrypted:

`VBoxManage showvminfo --password-id {{passwordid}} {{name|uuid}}`

- Specify the password file if the virtual machine is encrypted:

`VBoxManage showvminfo --password {{path/to/passwordfile}} {{name|uuid}}`

- Show the logs of a specific virtual machine:

`VBoxManage showvminfo --log {{name|uuid}}`
