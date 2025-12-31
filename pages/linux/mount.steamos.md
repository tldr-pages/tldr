# mount.steamos

> Mount or unmount SteamOS filesystem partitions.
> More information: <https://gitlab.com/users/evlaV/projects>.

- Mount all necessary partitions from a device to a target directory:

`sudo mount.steamos {{/dev/sdX}} {{/mnt}}`

- Mount with options to exclude specific partitions (e.g. `/home`, overlays):

`sudo mount.steamos {{[-o|--options]}} nohome,nooverlay {{/dev/sdX}} {{/mnt}}`

- Unmount all partitions mounted under a target directory:

`sudo mount.steamos -u {{/mnt}}`

- Display help:

`mount.steamos {{[-h|--help]}}`
