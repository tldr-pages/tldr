# swupd

> Package management utility for Clear Linux.
> More information: <https://docs.01.org/clearlinux/latest/guides/clear/swupd.html>.

- Update to latest version:

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
