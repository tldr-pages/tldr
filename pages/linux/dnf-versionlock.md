# dnf versionlock

> Protect packages from updates to newer versions.
> Locks are stored in `/etc/dnf/versionlock.toml`.
> More information: <https://dnf5.readthedocs.io/en/latest/commands/versionlock.8.html>.

- List the current versionlock entries:

`dnf versionlock list`

- Lock a package to the installed version, or to the currently available versions if it is not installed:

`sudo dnf versionlock add {{package}}`

- Exclude one available version from transactions:

`sudo dnf versionlock exclude {{package}}`

- Remove versionlock entries that match a package:

`sudo dnf versionlock delete {{package}}`

- Remove every versionlock entry:

`sudo dnf versionlock clear`
