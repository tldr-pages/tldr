# nix-build

> Erstellen eines Nix-Ausdrucks.
> Siehe auch: `nix build.3`.
> Weitere Informationen: <https://nix.dev/manual/nix/stable/command-ref/nix-build.html>.

- Erstelle einen Nix-Ausdruck:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- Erstelle einen gesandboxten Nix-Ausdruck (auf nicht-NixOS):

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
