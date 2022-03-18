# diskpart

> Disk, volume and partition manager.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Start diskpart (requires administrative rights):

`diskpart`

- Print all disks:

`list disk`

- Select the specified volume:

`select volume {{volume}}`

- Assign the drive letter to the selected volume:

`assign letter {{letter}}`

- Create the new partition:

`create partition primary`

- Activate the selected volume:

`active`

- Exit diskpart:

`exit`
