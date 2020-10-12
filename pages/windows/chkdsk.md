# chkdsk

> Check file system and volume metadata for errors.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Specify the drive letter (followed by a colon), mount point, or volume name to check:

`chkdsk {{volume}}`

- Fix errors on specified volume:

`chkdsk {{volume}} /f`

- Dismount a specific volume before checking:

`chkdsk {{volume}} /x`

- Use with NTFS only; change the log file size to the specified size:

`chkdsk /l{{size}}`
