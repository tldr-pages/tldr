# dnf system-upgrade

> Upgrade Fedora to a new major release.
> More information: <https://dnf5.readthedocs.io/en/latest/commands/system-upgrade.8.html>.

- Prepare the system by upgrading all installed packages:

`sudo dnf upgrade --refresh`

- Download packages required for the new release version:

`sudo dnf system-upgrade download --releasever {{release_version}}`

- Reboot and start the upgrade process:

`sudo dnf system-upgrade reboot`

- Display the status of the current upgrade transaction:

`sudo dnf system-upgrade status`

- Display logs from previous upgrade attempts:

`sudo dnf system-upgrade log`

- Remove cached upgrade data and packages:

`sudo dnf system-upgrade clean`
