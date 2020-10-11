# chkdsk

> Checks file system & volume metadata for errors.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk/>.

- Specify the drive letter (followed by a colon), mount point, or volume name to check:

`chkdsk {{volume}}`

- Fix errors on specified volume:

`chkdsk {{volume}} /f`

- Dismount specified volume before checking:

`chkdsk {{volume}} /x`

- Use with NTFS only; change the log file size to the specified size:

`chkdsk /l{{size}}`
