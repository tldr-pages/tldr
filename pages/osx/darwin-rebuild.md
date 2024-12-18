# darwin-rebuild

> Rebuild and switch to a Nix-based Darwin (macOS) system configuration.
> More information: <https://github.com/LnL7/nix-darwin>.

- Rebuild and switch to the specified Darwin configuration:

`darwin-rebuild switch --flake {{path/to/flake}}`

- Build the configuration but don't switch to it:

`darwin-rebuild build --flake {{path/to/flake}}`

- Display help:

`darwin-rebuild --help`
