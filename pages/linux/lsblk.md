# lsblk

> List information about devices.
> More information: <https://manned.org/lsblk>.

- List all storage devices in a tree-like format:

`lsblk`

- Also list empty devices:

`lsblk {{[-a|--all]}}`

- Print the SIZE column in bytes rather than in a human-readable format:

`lsblk {{[-b|--bytes]}}`

- Output info about filesystems:

`lsblk {{[-f|--fs]}}`

- Use ASCII characters for tree formatting:

`lsblk {{[-i|--ascii]}}`

- Output info about block-device topology:

`lsblk {{[-t|--topology]}}`

- Exclude the devices specified by the comma-separated list of major device numbers:

`lsblk {{[-e|--exclude]}} {{1,7,...}}`

- Display a customized summary using a comma-separated list of columns:

`lsblk {{[-o|--output]}} {{NAME,ROTA,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...}}`
