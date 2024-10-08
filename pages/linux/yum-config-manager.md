# yum-config-manager

> Manage DNF configuration options and repositories on Fedora-based systems.
> More information: <https://manned.org/yum-config-manager>.

- Add (and enable) a repository from a URL:

`dnf config-manager --add-repo={{url}}`

- Print current configuration values:

`dnf config-manager --dump`

- Enable a specific repository:

`dnf config-manager --set-enabled {{repoid}}`

- Disable specified repositories:

`dnf config-manager --set-disabled {{repoid1}} {{repoid2}}`

- Set a configuration option for a repository:

`dnf config-manager --setopt={{option}}={{value}}`

- Show help information:

`dnf config-manager --help-cmd`