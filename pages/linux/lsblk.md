# lsblk

> Lists information about devices.
> More information: <https://manned.org/lsblk>.

- List all storage devices in a tree-like format:

`lsblk`

- Also list empty devices:

`lsblk -a`

- Print the SIZE column in bytes rather than in a human-readable format:

`lsblk -b`

- Output info about filesystems:

`lsblk -f`

- Use ASCII characters for tree formatting:

`lsblk -i`

- Output info about block-device topology:

`lsblk -t`

- Exclude the devices specified by the comma-separated list of major device numbers:

`lsblk -e {{1,7,...}}`

- Display a customized summary using a comma-separated list of columns:

`lsblk --output {{NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...}}`
