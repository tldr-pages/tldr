# nh

> Nix Helper — a command-line tool for common NixOS, Home Manager, and macOS (nix-darwin) tasks.
> Provides unified subcommands to rebuild systems, manage home configs, search packages, and clean the Nix store.
> More information: <https://github.com/nix-community/nh>.

- Rebuild and activate the current NixOS configuration:
`nh os switch`

- Rebuild NixOS using a specific flake:
`nh os switch {{/path/to/flake}}`

- Rebuild and activate the current nix-darwin (macOS) configuration:
`nh darwin switch`

- Rebuild and activate the current Home Manager configuration:
`nh home switch`

- Rebuild Home Manager using a specific flake:
`nh home switch {{/path/to/flake}}`

- Clean old generations and unused store paths:
`nh clean all`

- Search for a package:
`nh search {{query}}`
