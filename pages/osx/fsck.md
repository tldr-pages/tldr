# fsck

> Check the integrity of a filesystem or repair it. The filesystem should be unmounted at the time the command is run.
> It is a wrapper that calls `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, and `fsck_udf` as needed.
> More information: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Check filesystem `/dev/sdX`, reporting any damaged blocks:

`fsck {{/dev/sdX}}`

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and interactively letting the user choose to repair each one:

`fsck -f {{/dev/sdX}}`

- Check filesystem `/dev/sdX` only if it is clean, reporting any damaged blocks and automatically repairing them:

`fsck -fy {{/dev/sdX}}`

- Check filesystem `/dev/sdX`, reporting whether it has been cleanly unmounted:

`fsck -q {{/dev/sdX}}`
