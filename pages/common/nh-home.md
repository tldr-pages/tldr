# nh home

> Manage and configure per-user environment using Nix.
> Reimplementation of `home-manager`.
> More information: <https://github.com/nix-community/nh#usage>.

- Build and switch to a specified Home Manager flake configuration:

`nh home switch {{path/to/flake}}`

- Update all the flake inputs of the specified Home Manager flake configuration and build it:

`nh home build {{path/to/flake}} {{[-u|--update]}}`

- Load a specified Home Manager flake configuration in Nix REPL (Nix evaluation environment):

`nh home repl {{path/to/flake}}`
