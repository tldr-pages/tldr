# nix-instantiate

> Create store derivations from nix expressions.
> For more human readable output see: `nix eval`.
> More information: <https://nix.dev/manual/nix/2.28/command-ref/nix-instantiate.html>.

- Evaluate an expression:

`nix-instantiate {{--eval}} {{--expr}} {{expr}}`

- To evaluate with machine readable output:

`nix-instantiate {{--eval}} {{--xml}} {{-expr}} {{expr}}`

- Raw output, output of the function must be a string:

`nix-instantiate {{--eval}} {{--raw}} {{--expr}} {{expr}}`

- Evaluate a file:

`nix-instantiate {{--eval}} {{file.nix}}`
