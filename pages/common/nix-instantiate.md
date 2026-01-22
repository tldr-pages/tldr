# nix-instantiate

> Create store derivations from nix expressions.
> See also: `nix eval`.
> More information: <https://nix.dev/manual/nix/2.28/command-ref/nix-instantiate.html>.

- Evaluate an expression:

`nix-instantiate --eval {{[-E|--expr]}} {{expression}}`

- Evaluate with machine readable output:

`nix-instantiate --eval --xml {{[-E|--expr]}} {{expression}}`

- Raw output, output of the function must be a string:

`nix-instantiate --eval --raw {{[-E|--expr]}} {{expression}}`

- Evaluate a file:

`nix-instantiate --eval {{file.nix}}`
