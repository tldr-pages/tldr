# dnf config-manager

> Manage DNF configuration options and repositories on Fedora-based systems.
> More information: <https://manned.org/dnf-config-manager>.

- Add (and enable) a repository from a URL:

`dnf config-manager --add-repo={{repository_url}}`

- Print current configuration values:

`dnf config-manager --dump`

- Enable a specific repository:

`dnf config-manager --set-enabled {{repository_id}}`

- Disable specified repositories:

`dnf config-manager --set-disabled {{repository_id1 repository_id2 ...}}`

- Set a configuration option for a repository:

`dnf config-manager --setopt={{option}}={{value}}`

- Display help:

`dnf config-manager --help-cmd`
