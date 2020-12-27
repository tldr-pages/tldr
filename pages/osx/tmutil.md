# tmutil

> Utility for managing Time Machine backups. Most verbs require root privileges.

- Set a HFS+ drive as the backup destination:

`sudo tmutil setdestination {{path/to/disk_mount_point}}`

- Set a APF share or SMB share as the backup destination:

`sudo tmutil setdestination {{protocol://user[:pass]@host/share}}`

- Set a APF share or SMB share as the backup destination, but input the password in a non-echoing prompt:

`sudo tmutil setdestination -p {{protocol://user@host/share}}`

- Append the given destination to the list of destinations

`sudo tmutil setdestination -a {{destination}}`

- Print information about destinations currently configured for use with Time Machine:

`tmutil destinationinfo`

> If you wish for the output to be in XML property format, add the "-X" option.

> For each backup destination, the following information may be displayed:
>     Name --------- The volume label as shown in Finder.

>     Kind --------- Whether the destination is locally attached
>                    storage or a network device.

>     URL ---------- In the case of a network destination, the URL
>                    used for Time Machine configuration.

>     Mount Point -- If the volume is currently mounted, the path in
>                    the file system at which it was mounted.

>     ID ----------- The unique identifier for the destination.

>          
> When more than one destination is configured, the most recent
> backup destination will be marked with the ">" indicator.

- Remove the destination with the specified unique identifier from the Time Machine configuration:

`tmutil removedestination {{UUID}}`

- Add a file or folder to the exclusion list, to be excluded from backups:

`tmutil addexclusion {{file_or_directory}}`

> The -p option configures fixed-path exclusions. The -v option configures volume exclusions. Both require root privileges. The -v option is the only supported way to exclude or unexclude a volume; behavior is undefined if a sticky or fixed-path exclusion is specified.
