# home-manager

> Manage a per-user environment using Nix, allowing declarative configuration of the user's home.
> More information: <https://github.com/nix-community/home-manager>.

- Build the configuration defined in `~/.config/nixpkgs/home.nix` without applying it:

`home-manager build`

- Build and apply (switch to) the new configuration:

`home-manager switch`

- Roll back to a previous configuration generation:

`home-manager rollback`

- List all existing configuration generations:

`home-manager generations`

- When using flakes, run any operation that requires nix to run (build, switch, news) by passing the path to the flake:

`home-manager {{command}} --flake {{path/to/flake}}`
