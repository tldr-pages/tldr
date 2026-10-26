# dnf config-manager

> Manage DNF5 configuration, repositories, and variables.
> Repository edits are written as drop-in overrides. Existing `.repo` files are not modified.
> More information: <https://dnf5.readthedocs.io/en/latest/dnf5_plugins/config-manager.8.html>.

- Add repositories from a `.repo` file:

`sudo dnf config-manager addrepo --from-repofile={{https://example.com/file.repo}}`

- Add a repository with a base URL:

`sudo dnf config-manager addrepo --set=baseurl={{https://example.com/repo}} --id={{repository_id}}`

- Enable a repository:

`sudo dnf config-manager enable {{repository_id}}`

- Disable repositories:

`sudo dnf config-manager disable {{repository_id1 repository_id2 ...}}`

- Set a main configuration option (for example, keep downloaded packages):

`sudo dnf config-manager setopt keepcache=1`

- Set a per-repository option:

`sudo dnf config-manager setopt {{repository_id}}.{{option}}={{value}}`

- Set a variable used in repository configuration:

`sudo dnf config-manager setvar {{name}}={{value}}`
