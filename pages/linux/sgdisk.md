# sgdisk

> A command-line partitioning tool for GPT disks.
> Part of the `gdisk` package.

- Show partition table:
`sgdisk -p {{/dev/sdX}}`

- Create a new partition:
`sgdisk -n {{1}}:{{start}}:{{end}} {{/dev/sdX}}`

- Delete a partition:
`sgdisk -d {{1}} {{/dev/sdX}}`

- Backup the GPT table:
`sgdisk -b {{backup.img}} {{/dev/sdX}}`

- Restore the GPT table:
`sgdisk -l {{backup.img}} {{/dev/sdX}}`
