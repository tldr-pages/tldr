# nix eval

> Evaluate a Nix expression and prints the result on stdout.
> More information: <https://nix.dev/manual/nix/2.28/command-ref/new-cli/nix3-eval.html>.

- Evaluate Nix flake attributes in the current directory:

`nix eval .#{{attributes}}`

- Evaluate a given Nix expression:

`nix eval --expr '{{your_expression}}'`

- Evaluate a Nix expression from a specified file:

`nix eval --file {{path/to/file}}`

- Print the store path of the specified package from nixpkgs:

`nix eval {{nixpkgs#pkg}} --raw`

- Evaluate attributes from a flake directly from GitHub:

`nix eval {{github:owner/repo#attributes}}`

- Evaluate the lambda specified lambda function passing the specified package as argument:

`nix eval {{nixpkgs#pkg}} --apply '{{lambda_function}}'`
