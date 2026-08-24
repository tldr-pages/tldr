# nh

> Modern helper utility tool for the Nix/NixOS ecosystem.
> Some subcommands such as `os`, `home`, `clean`, `search` have their own usage documentation.
> More information: <https://github.com/nix-community/nh#usage>.

- Build and switch to a specified NixOS flake configuration:

`nh os switch {{path/to/flake}}`

- Build and switch to a specified Home Manager flake configuration:

`nh home switch {{path/to/flake}}`

- Build and switch to a nix-darwin flake configuration:

`nh darwin switch {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Collect all garbage and gcroots from the Nix store:

`nh clean all {{[-a|--ask]}}`

- Search for a package in Nixpkgs:

`nh search {{name}}`

- Generate shell completions for a specified shell:

`nh completions {{shell}}`
