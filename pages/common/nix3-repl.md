# nix repl

> Start an interactive environment for evaluating Nix expressions.
> See <https://nixos.org/manual/nix/stable/language/index.html> for a description of the Nix expression language.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- Load all packages from a flake (e.g. `nixpkgs`) into scope:

`:lf {{nixpkgs}}`

- Build a package from an expression:

`:b {{expression}}`

- Start a shell with package from the expression available:

`:u {{expression}}`

- Start a shell with dependencies of the package from the expression available:

`:s {{expression}}`
