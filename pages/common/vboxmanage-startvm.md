# vboxmanage-startvm

> Start a virtual machine.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>.

- Start a virtual machine:

`VBoxManage startvm {{name|uuid}}`

- Start a virtual machine with the specified UI mode:

`VBoxManage startvm {{name|uuid}} --type {{headless|gui|sdl|separate}}`

- Specify a password file to start an encrypted virtual machine:

`VBoxManage startvm {{name|uuid}} --password {{path/to/passwordfile}}`

- Specify a password id to start an encrypted virtual machine:

`VBoxManage startvm  {{name|uuid}} --password-id {{passwordid}}`

- Start a vm with an environment variable pair name value:

`VBoxManage startvm  {{name|uuid}} --put-env={{name}}={{value}}`
