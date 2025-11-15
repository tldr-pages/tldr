# chkdsk

> Check file system and volume metadata for errors.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Specify the drive letter (followed by a colon), mount point, or volume name to check:

`chkdsk {{volume}}`

- Fix errors on a specific volume:

`chkdsk {{volume}} /f`

- Dismount a specific volume before checking:

`chkdsk {{volume}} /x`

- Change the log file size to the specified size (only for NTFS):

`chkdsk /l{{size}}`
