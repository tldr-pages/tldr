# pdisk

> Edit Apple partition maps on disks.
> See also: `diskutil`, `fdisk`.
> More information: <https://keith.github.io/xcode-man-pages/pdisk.8.html>.

- List partition maps for one or more devices:

`pdisk {{[-l|--list]}} {{/dev/disk}}`

- Start interactive partition editing for a device:

`pdisk {{[-i|--interactive]}} {{/dev/disk}}`

- Open a device read-only:

`pdisk {{[-r|--readonly]}} {{/dev/disk}}`

- Show HFS volume names instead of partition names:

`pdisk {{[-f|--fname]}} {{[-l|--list]}} {{/dev/disk}}`

- Display help:

`pdisk {{[-h|--help]}}`

- Display version:

`pdisk {{[-v|--version]}}`
