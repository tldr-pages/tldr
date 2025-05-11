# nix-build

> Build a Nix expression.
> See also: `nix build.3`.
> More information: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Build a Nix expression:

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}}`

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{firefox}} --option sandbox true`
