# ocamlfind

> The findlib package manager for OCaml.
> Simplifies linking executables with external libraries.
> More information: <http://projects.camlcity.org/projects/findlib.html>.

- Compile a source file to a native binary and link with packages:

`ocamlfind ocamlopt -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Compile a source file to a bytecode binary and link with packages:

`ocamlfind ocamlc -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Cross-compile for a different platform:

`ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{executable}} {{source_file.ml}}`
