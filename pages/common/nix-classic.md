# nix classic

> A classic, stable interface to a powerful package manager that makes package management reliable, reproducible, and declarative.
> Some Nix commands such as `nix-build`, `nix-shell`, `nix-env`, and `nix-store` have their own pages.
> See also: `nix`.
> More information: <https://nixos.org>.

- Search for a package in nixpkgs via its name:

`nix-env {{[-qaP|--query --available --attr-path]}} {{search_term_regex}}`

- Start a shell with the specified packages available:

`nix-shell {{[-p|--packages]}} {{pkg1 pkg2 pkg3 ...}}`

- Install some packages permanently:

`nix-env {{[-iA|--install --attr]}} {{nixpkgs.pkg1 nixpkgs.pkg2 ...}}`

- Show all dependencies of a store path (package), in a tree format:

`nix-store {{[-q|--query]}} --tree /nix/store/{{checksum-package-version.ext}}`

- Update the channels (repositories):

`nix-channel --update`

- Remove unused paths from Nix store:

`nix-collect-garbage`
