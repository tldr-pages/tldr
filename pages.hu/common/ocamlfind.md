# ocamlfind

> A findlib csomagkezelő az OCaml-hoz. Egyszerűsíti a futtatható programok külső könyvtárakkal való összekapcsolását. További információ: <http://projects.camlcity.org/projects/findlib.html>.

- Egy forrásfájlt natív bináris állományba fordít és csomagokkal linkel:

`ocamlfind ocamlopt -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Egy forrásfájl fordítása bytecode binárisra és összekapcsolása csomagokkal:

`ocamlfind ocamlc -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}`

- Keresztkompilálás más platformra:

`ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{executable}} {{source_file.ml}}`
