# nix-env

> Manipulate or query Nix user environments.
> More information: <https://nixos.org/releases/nix/latest/manual#sec-nix-env>.

- List all installed packages:

`nix-env -q`

- Query installed packages:

`nix-env -q {{search_term}}`

- Query available packages:

`nix-env -qa {{search_term}}`

- Install package:

`nix-env -i {{pkg_name}}`

- Uninstall package:

`nix-env -e {{pkg_name}}`

- Upgrade one package:

`nix-env -u {{pkg_name}}`

- Upgrade all packages:

`nix-env -u`
