# dnf config-manager

> Manage DNF configuration options and repositories on Fedora-based systems.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- Add (and enable) a repository from a URL:

`dnf config-manager --add-repo={{repository_url}}`

- Print current configuration values:

`dnf config-manager --dump`

- Enable a specific repository:

`dnf config-manager {{[--enable|--set-enabled]}} {{repository_id}}`

- Disable specified repositories:

`dnf config-manager {{[--disable|--set-disabled]}} {{repository_id1 repository_id2 ...}}`

- Set a configuration option for a repository:

`dnf config-manager --setopt={{option}}={{value}}`

- Display help:

`dnf config-manager --help-cmd`
