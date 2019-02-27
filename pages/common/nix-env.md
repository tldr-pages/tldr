# nix-env

> Manipulate or query Nix user environments.

- Show installed packages:

`nix-env -q`

- Query available packages:

`nix-env -qa {{pkg_name}}`

- Query the status of available packages:

`nix-env -qsa`

- Install package:

`nix-env -i {{pkg_name}}`

- Uninstall package:

`nix-env -e {{pkg_name}}`

- Upgrade one package:

`nix-env -u {{pkg_name}}`

- Upgrade all packages:

`nix-env -u`
