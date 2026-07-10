# dnf copr

> Manage Copr repositories on Fedora-based systems.
> Provided by `dnf-plugins-core`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/copr.html>.

- Enable a Copr repository:

`sudo dnf copr enable {{owner}}/{{project}}`

- Enable a Copr repository for a specific chroot:

`sudo dnf copr enable {{owner}}/{{project}} {{fedora-rawhide-x86_64}}`

- Disable a Copr repository:

`sudo dnf copr disable {{owner}}/{{project}}`

- Remove a Copr repository:

`sudo dnf copr remove {{owner}}/{{project}}`

- List Copr repositories:

`dnf copr list {{[--installed|--enabled|--disabled]}}`

- List Copr repositories available from a user:

`dnf copr list --available-by-user {{owner}}`

- Search for a Copr project:

`dnf copr search {{project}}`
