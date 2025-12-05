# nix-env

> Manipulate or query Nix user environments.
> More information: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- List all installed packages:

`nix-env {{[-q|--query]}}`

- Query installed packages (regex is supported):

`nix-env {{[-q|--query]}} {{search_pattern}}`

- Query available packages from the NixPkgs registry:

`nix-env {{[-qa|--query --available]}} {{search_pattern}}`

- Install a package from the NixPkgs registry:

`nix-env {{[-iA|--install --attr]}} nixpkgs.{{pkg_name}}`

- Install a package from a custom URL:

`nix-env {{[-i|--install]}} {{pkg_name}} {{[-f|--file]}} {{example.com}}`

- Uninstall a package:

`nix-env {{[-e|--uninstall]}} {{pkg_name}}`

- Upgrade a package:

`nix-env {{[-u|--upgrade]}} {{pkg_name}}`

- Get usage help for a specific operation (`--install`, `--upgrade`, etc.):

`nix-env {{--help}} --{{option_name}}`
