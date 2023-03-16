# nix why-depends

> Show why a package depends on another package.

- Show why the currently running NixOS system requires a certain store path:

`nix why-depends {{/run/current-system}} {{/nix/store/...}}`

- Show why a package from nixpkgs requires another package as a _build-time_ dependency:

`nix why-depends --derivation {{nixpkgs#dependent}} {{nixpkgs#dependency}}`
