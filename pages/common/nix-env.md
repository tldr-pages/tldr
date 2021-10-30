# nix-env

> Manipulate or query Nix user environments.
> More information: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- List all installed packages:

`nix-env -q`

- Query installed packages:

`nix-env -q {{search_term}}`

- Query available packages:

`nix-env -qa {{search_term}}`

- Install package:

`nix-env -iA nixpkgs.{{pkg_name}}`

- Install a package from a URL:

`nix-env -i {{pkg_name}} --file {{example.com}}`

- Uninstall package:

`nix-env -e {{pkg_name}}`

- Upgrade one package:

`nix-env -u {{pkg_name}}`

- Upgrade all packages:

`nix-env -u`
