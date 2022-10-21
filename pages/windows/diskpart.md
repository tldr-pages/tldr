# diskpart

> Disk, volume and partition manager.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Run diskpart by itself in an administrative command prompt to enter its command line:

`diskpart`

- List all disks:

`list disk`

- Select a volume:

`select volume {{volume}}`

- Assign a drive letter to the selected volume:

`assign letter {{letter}}`

- Create a new partition:

`create partition primary`

- Activate the selected volume:

`active`

- Exit diskpart:

`exit`
