# vboxmanage

> Command-line interface for managing VirtualBox virtual machines on Windows.
> More information: https://www.virtualbox.org/manual/ch08.html

- Show information about all virtual machines:
`vboxmanage list vms`

- Start a specific VM:
`vboxmanage startvm {{vm_name}}`

- Power-off a running VM:
`vboxmanage controlvm {{vm_name}} poweroff`

- Show running virtual machines:
`vboxmanage list runningvms`

- Create a new VM:
`vboxmanage createvm --name {{vm_name}} --register`
