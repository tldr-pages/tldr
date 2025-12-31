# tune.exfat

> Adjust tunable filesystem parameters on an exFAT filesystem.
> More information: <https://manned.org/tune.exfat>.

- Print the volume label of a filesystem:

`tune.exfat {{[-l|--print-label]}} {{/dev/sdXY}}`

- Set the volume label of a filesystem:

`tune.exfat {{[-L|--set-label]}} {{new_label}} {{/dev/sdXY}}`

- Print the volume GUID of a filesystem:

`tune.exfat {{[-u|--print-guid]}} {{/dev/sdXY}}`

- Set the volume GUID of a filesystem:

`tune.exfat {{[-U|--set-guid]}} {{new_guid}} {{/dev/sdXY}}`

- Print the volume serial of a filesystem:

`tune.exfat {{[-i|--print-serial]}} {{/dev/sdXY}}`

- Set the volume serial of a filesystem:

`tune.exfat {{[-I|--set-serial]}} {{new_serial}} {{/dev/sdXY}}`
