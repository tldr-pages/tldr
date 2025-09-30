# nix

> A powerful package manager that makes package management reliable, reproducible, and declarative.
> `nix` is experimental and requires enabling experimental features.
> See also: `nix classic` for a classic, stable interface.
> Some subcommands such as `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends`, etc. have their own usage documentation.
> More information: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>.

- Enable the `nix` command:

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

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

- Display help for a specific subcommand:

`nix help {{subcommand}}`
