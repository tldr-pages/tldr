# nix-env

> Manipulate or query Nix user environments.

- Show available package with name or without name:

`nix-env -qa {{pkg_name}}`

- Show the status of available packages:

`nix-env -qas`

- Install package:

`nix-env -i {{pkg_name}}`

- Uninstall package:

`nix-env -e {{pkg_name}}`

- Upgrade one package:

`nix-env -u {{pkg_name}}`

- Upgrade all packages:

`nix-env -u`
