# chkdsk

> Check file system and volume metadata for errors.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Check the specified drive, mount point, or volume name for errors:

`chkdsk {{drive:|mount_point|volume_name}}`

- Repair the specified volume:

`chkdsk {{volume}} /f`

- Dismount the specified volume before checking:

`chkdsk {{volume}} /x`

- Set the log file size to the specified size (only for NTFS):

`chkdsk /l:{{size}}`
