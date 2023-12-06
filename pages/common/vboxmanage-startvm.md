# vboxmanage-startvm

> Start a virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>.

- Start a virtual machine:

`VBoxManage startvm {{vm_name|uuid}}`

- Start a virtual machine with the specified UI mode:

`VBoxManage startvm {{vm_name|uuid}} --type {{headless|gui|sdl|separate}}`

- Specify a password file to start an encrypted virtual machine:

`VBoxManage startvm {{vm_name|uuid}} --password {{path/to/password_file}}`

- Specify a password ID to start an encrypted virtual machine:

`VBoxManage startvm  {{vm_name|uuid}} --password-id {{password_id}}`

- Start a virtual machine with an environment variable pair name value:

`VBoxManage startvm  {{vm_name|uuid}} --put-env={{name}}={{value}}`
