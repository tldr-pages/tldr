# upgradepkg

> Upgrade Slackware packages by replacing existing packages with new versions.
> See also: `installpkg`, `removepkg`, `makepkg`, `pkgtool`.
> More information: <https://slackware.nl/slackware/slackware64-current/source/a/pkgtools/manpages/upgradepkg.8>.

- Upgrade a package:

`sudo upgradepkg {{path/to/package.tgz}}`

- Upgrade a package, installing it if not already present:

`sudo upgradepkg --install-new {{path/to/package.tgz}}`

- Reinstall a package (even if the same version is already installed):

`sudo upgradepkg --reinstall {{path/to/package.tgz}}`

- Preview what would happen without actually upgrading:

`upgradepkg --dry-run {{path/to/package.tgz}}`

- Upgrade a package and show detailed progress:

`sudo upgradepkg --verbose {{path/to/package.tgz}}`
