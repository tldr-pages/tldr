# ocamlfind

> Managerul de pachete findlib pentru oCl.
> Simplifică legarea executabilelor cu bibliotecile externe.
> Mai multe informaţii: <http://projects.camlcity.org/projects/findlib.html>

- Compilați un fișier sursă la un binar nativ și legați cu pachetele:

`ocamlfind ocamlopt -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Compilați un fișier sursă la un binar bytecode și legați cu pachete:

`ocamlfind ocamlc -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Compilare încrucișată pentru o altă platformă:

`ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{executable}} {{source_file.ml}}`
