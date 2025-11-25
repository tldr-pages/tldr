# sgdisk

> Manage GUID Partition Tables (GPT).
> Part of the GPT fdisk suite; designed for scripting and automation.
> More information: <https://manned.org/sgdisk>.

- Display basic GPT partition summary data for a device:

`sudo sgdisk {{[-p|--print]}} {{/dev/sdX}}`

- Wipe both GPT and MBR data structures from a device (destroys all partition information):

`sudo sgdisk {{[-Z|--zap-all]}} {{/dev/sdX}}`

- Convert a GPT disk to MBR format using up to four partitions:

`sudo sgdisk {{[-m|--gpttombr]}} {{1:2:3:4}} {{/dev/sdX}}`

- Delete a partition entry by number (data in sectors remains untouched):

`sudo sgdisk {{[-d|--delete]}} {{1}} {{/dev/sdX}}`

- Save the current in-memory GPT data (protective MBR, headers, and table) to a binary backup file:

`sudo sgdisk {{[-b|--backup]}} {{/path/to/backup.gpt}} {{/dev/sdX}}`

- Load GPT data from a backup file (restoring from a non-original disk is not recommended):

`sudo sgdisk {{[-l|--load-backup]}} {{/path/to/backup.gpt}} {{/dev/sdX}}`

- Verify GPT structures for CRC errors, mismatches, or inconsistencies:

`sudo sgdisk {{[-v|--verify]}} {{/dev/sdX}}`

- Display a summary of available partition type codes (no device required):

`sgdisk {{[-L|--list-types]}}`
