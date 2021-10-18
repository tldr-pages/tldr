# diskpart

> Disk, volume and partition manager.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Run diskpart by itself in an administrative command prompt to enter its command line:

`diskpart`

- List all disks:

`list disk`

- Assign a drive letter to the selected volume:

`select volume {{volume}}`

Then:

`assign letter {{letter}}`

- Create a new partition:

`create partition primary`

- Activate a volume:

`select volume {{volume}}`

Then:

`active`

- Exit diskpart:

`exit`
