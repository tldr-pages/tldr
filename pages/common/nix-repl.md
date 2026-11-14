# nix repl

> Start an interactive environment for evaluating Nix expressions.
> See <https://nixos.org/manual/nix/stable/language/index.html> for a description of the Nix expression language.
> More information: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- [Interactive] Load all packages from a flake (e.g. `nixpkgs`) into scope:

`:lf {{nixpkgs}}`

- [Interactive] Build a package from an expression:

`:b {{expression}}`

- [Interactive] Start a shell with package from the expression available:

`:u {{expression}}`

- [Interactive] Start a shell with dependencies of the package from the expression available:

`:s {{expression}}`
