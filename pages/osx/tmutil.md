# tmutil

> Utility for managing Time Machine backups. Most verbs require root privileges.
> More information: <https://ss64.com/osx/tmutil.html>.

- Set an HFS+ drive as the backup destination:

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- Set an APF share or SMB share as the backup destination:

`sudo tmutil setdestination "{{protocol://user[:password]@host/share}}"`

- Append the given destination to the list of destinations:

`sudo tmutil setdestination -a {{destination}}`

- Enable automatic backups:

`sudo tmutil enable`

- Disable automatic backups:

`sudo tmutil disable`

- Start a backup, if one is not running already, and release control of the shell:

`sudo tmutil startbackup`

- Start a backup and block until the backup is finished:

`sudo tmutil startbackup -b`

- Stop a backup:

`sudo tmutil stopbackup`
