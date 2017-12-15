# fsck

> Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run.
> It is a wrapper that calls `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, and `fsck_udf` as needed.

- Check filesystem /dev/sda, reporting any damaged blocks:

`fsck {{/dev/sda}}`

- Check filesystem /dev/sda only if it is clean, reporting any damaged blocks and interactively letting the user choose to repair each one:

`fsck -f {{/dev/sda}}`

- Check filesystem /dev/sda only if it is clean, reporting any damaged blocks and automatically repairing them:

`fsck -fy {{/dev/sda}}`

- Check filesystem /dev/sda, reporting whether it has been cleanly unmounted:

`fsck -q {{/dev/sda}}`
