# diskpart

> Disk, volume, and partition manager.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Run diskpart by itself in an administrative command prompt to enter its command-line:

`diskpart`

- [Interactive] List all disks:

`list disk`

- [Interactive] Select a volume:

`select volume {{volume}}`

- [Interactive] Assign a drive letter to the selected volume:

`assign letter {{letter}}`

- [Interactive] Create a new partition:

`create partition primary`

- [Interactive] Activate the selected volume:

`active`

- [Interactive] Exit diskpart:

`exit`
