# nh

> Nix Helper — a command-line tool for common NixOS, Home Manager, and macOS (nix-darwin) tasks.
> Provides unified subcommands to rebuild systems, manage home configs, search packages, and clean the Nix store.
> More information: <https://github.com/nix-community/nh>.

- nh search - Searching tool
`nh os switch`

- nh clean - a re-implementation of nix-collect-garbage that also collects gcroots
`nh clean all --ask`

- nh os - reimplements nixos-rebuild with build-tree displays, diff of changes, confirmation
`nh os switch -- ask --file ./`

- nh home - reimpliments home-manager

- nh darwin - impliments darwin-rebuild
