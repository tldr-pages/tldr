# nix

> Powerful package manager that makes package management reliable, reproducible, and declarative.
> The `nix` command-line utility is experimental and requires enabling experimental features. For a classic, stable interface, see `tldr nix classic`.
> Some `nix` subcommands such as `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends` etc. have their own usage documentation, accessible via `tldr nix3 subcommand`.
> More information: <https://nixos.org/manual/nix>.

- Enable the `nix` command:

`mkdir -p ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Display help for the `nix` subcommand:

`nix help {{subcommand}}`

- Search for a package in nixpkgs via its name or description:

`nix search nixpkgs {{search_term}}`

- Start a shell with the specified packages from nixpkgs available:

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Install some packages from nixpkgs permanently:

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Remove unused paths from Nix store to free up space:

`nix store gc`

- Start an interactive environment for evaluating Nix expressions:

`nix repl`
