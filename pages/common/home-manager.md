# home-manager

> Manage a per-user environment using Nix, allowing declarative configuration of the user’s home.
> More information: <https://github.com/nix-community/home-manager>.

- Build the configuration defined in `~/.config/nixpkgs/home.nix` without applying it:

`home-manager build`

- Build and apply (switch to) the new configuration:

`home-manager switch`

- Build the configuration for testing without applying it:

`home-manager test`

- Roll back to a previous configuration generation:

`home-manager rollback`

- List all existing configuration generations:

`home-manager generations`
