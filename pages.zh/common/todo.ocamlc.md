# ocamlc

> The OCaml bytecode compiler.
> Produces executables runnable by the OCaml interpreter.
> More information: <https://ocaml.org>.

- Create a binary from a source file:

`ocamlc {{path/to/source_file.ml}}`

- Create a named binary from a source file:

`ocamlc -o {{path/to/binary}} {{path/to/source_file.ml}}`

- Automatically generate a module signature (interface) file:

`ocamlc -i {{path/to/source_file.ml}}`
