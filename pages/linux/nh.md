# nh

> Modern helper utility tool for the Nix/Nixos ecosystem.
> More information: <https://github.com/nix-community/nh#usage>.

- Search for a package in Nixpkgs, limiting results:

`nh search {{[-l|--limit]}} {{number}} {{name}}`

- Collect all garbage and gcroots from the Nix store:

`nh clean all {{[-a|--ask]}}`

- Build the specified nixos flake configuration and open it in a virtual machine:

`nh os build-vm {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Build and switch to the specified home-manager flake configuration:

`nh home switch {{path/to/flake}} {{[-c|--configuration]}} {{home}}`

- Build and switch to a nix-darwin flake configuration:

`nh darwin switch {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Generate shell completions for a specified shell:

`nh completions {{shell}}`
