# ocamlfind

> OCaml 的 findlib 包管理器。
> 简化了可执行文件与外部库的链接。
> 更多信息：<https://projects.camlcity.org/projects/findlib.html>。

- 将源文件编译为本地二进制文件并与包链接：

`ocamlfind ocamlopt -package {{package1}},{{package2}} -linkpkg -o {{path/to/executable}} {{path/to/source.ml}}`

- 将源文件编译为字节码二进制文件并与包链接：

`ocamlfind ocamlc -package {{package1}},{{package2}} -linkpkg -o {{path/to/executable}} {{path/to/source.ml}}`

- 为不同平台交叉编译：

`ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{path/to/executable}} {{path/to/source.ml}}`