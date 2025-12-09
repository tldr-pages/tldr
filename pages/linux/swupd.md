# swupd

> Package management utility for Clear Linux.
> More information: <https://www.clearlinux.org/clear-linux-documentation/guides/clear/swupd.html>.

- Update to the latest version:

`sudo swupd update`

- Show current version, and check whether a newer one exists:

`swupd check-update`

- List installed bundles:

`swupd bundle-list`

- Locate the bundle where a wanted package exists:

`swupd search -b {{package}}`

- Install a new bundle:

`sudo swupd bundle-add {{bundle}}`

- Remove a bundle:

`sudo swupd bundle-remove {{bundle}}`

- Correct broken or missing files:

`sudo swupd verify`
