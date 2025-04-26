# nix-env

> Manipulate or query Nix user environments.
> More information: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- List all installed packages:

`nix-env {{[-q|--query]}}`

- Query installed packages:

`nix-env {{[-q|--query]}} {{search_term}}`

- Query available packages:

`nix-env {{[-qa|--query --available]}} {{search_term}}`

- Install package:

`nix-env {{[-iA|--install --attr]}} nixpkgs.{{pkg_name}}`

- Install a package from a URL:

`nix-env {{[-i|--install]}} {{pkg_name}} {{[-f|--file]}} {{example.com}}`

- Uninstall package:

`nix-env {{[-e|--uninstall]}} {{pkg_name}}`

- Upgrade one package:

`nix-env {{[-u|--upgrade]}} {{pkg_name}}`

- Upgrade all packages:

`nix-env {{[-u|--upgrade]}}`
