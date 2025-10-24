# cleanmgr

> Clear unnecessary files from the computer's hard disk.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cleanmgr>.

- Open Disk Cleanup for a specific drive:

`cleanmgr {{/d|/D}} {{C}}`

- Open Disk Cleanup with all options selected by default:

`cleanmgr {{/d|/D}} {{C}} /lowdisk`

- Clean up all files automatically without user prompts:

`cleanmgr {{/d|/D}} {{C}} /verylowdisk`

- Configure which files to clean and save the settings to a specific profile:

`cleanmgr /sageset:{{profile_number}}`

- Run Disk Cleanup using a previously configured profile:

`cleanmgr /sagerun:{{profile_number}}`

- Clean up files left after a Windows upgrade:

`cleanmgr /autoclean`

- Clean up files from a previous Windows installation:

`cleanmgr /setup`

- Display help:

`cleanmgr /?`
