# dnf5 copr

> Manage Copr repositories on Fedora-based systems.
> More information: <https://dnf5.readthedocs.io/en/latest/dnf5_plugins/copr.8.html>.

- Enable a Copr repository:

`sudo dnf5 copr enable {{owner}}/{{project}}`

- Enable a Copr repository for a specific chroot:

`sudo dnf5 copr enable {{owner}}/{{project}} {{fedora-rawhide-ppc64le}}`

- Enable a Copr repository from a specific hub:

`sudo dnf5 copr enable {{hub}}/{{owner}}/{{project}}`

- Disable a Copr repository:

`sudo dnf5 copr disable {{owner}}/{{project}}`

- Remove a Copr repository:

`sudo dnf5 copr remove {{owner}}/{{project}}`

- List Copr repositories:

`dnf5 copr list`

- Print debug information about the system:

`dnf5 copr debug`
