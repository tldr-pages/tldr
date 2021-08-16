# synoupgrade

> Upgrade a Synology DiskStation Manager (DSM) from the command-line.
> More information: <https://www.synology.com/dsm>.

- Check if upgrades are available:

`sudo synoupgrade --check`

- Check for patches without upgrading the DSM version:

`sudo synoupgrade --check-smallupdate`

- Download the latest upgrade available (use `--download-smallupdate` for patches):

`sudo synoupgrade --download`

- Start the upgrade process:

`sudo synoupgrade --start`

- Upgrade to the latest version automatically:

`sudo synoupgrade --auto`

- Apply patches without upgrading the DSM version automatically:

`sudo synoupgrade --auto-smallupdate`

- Upgrade the DSM using a patch file (should be an absolute path):

`sudo synoupgrade --patch {{/path/to/file.pat}}`

- Display help:

`synoupgrade`
