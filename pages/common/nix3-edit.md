# nix edit

> Open the Nix expression of a Nix package in $EDITOR.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- Open the source of the Nix expression of a package from nixpkgs in your `$EDITOR`:

`nix edit {{nixpkgs#pkg}}`

- Dump the source of a package to `stdout`:

`EDITOR=cat nix edit {{nixpkgs#pkg}}`
