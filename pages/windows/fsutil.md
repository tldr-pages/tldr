# fsutil

> Displays information about file system volumes.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- Display a list of volumes:

`fsutil volume list`

- Displays information about a volume‘s file system:

`fsutil fsInfo volumeInfo {{drive_letter|volume_path}}`

- Display the current state of file system auto-repair for all volumes:

`fsutil repair state`

- Display the dirty bit state of all volumes:

`fsutil dirty query`

- Set the dirty bit state of a volume:

`fsutil dirty set {{drive letter | volume path}}`
