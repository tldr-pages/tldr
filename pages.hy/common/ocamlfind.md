# ocamlfind

> Findlib փաթեթի կառավարիչ OCaml-ի համար:.
> Պարզեցնում է գործադիրների կապը արտաքին գրադարանների հետ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ocamlfind>:.

- Կազմել սկզբնաղբյուր ֆայլը բնիկ երկուականին և կապել փաթեթների հետ.:

`ocamlfind ocamlopt -package {{package1,package2,...}} -linkpkg -o {{path/to/executable}} {{path/to/source.ml}}`

- Կազմել աղբյուրի ֆայլը բայթկոդի երկուական և կապել փաթեթների հետ.:

`ocamlfind ocamlc -package {{package1,package2,...}} -linkpkg -o {{path/to/executable}} {{path/to/source.ml}}`

- Cross-compile մեկ այլ հարթակի համար.:

`ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{path/to/executable}} {{path/to/source.ml}}`
