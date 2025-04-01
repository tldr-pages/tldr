# ocamlc

> OCaml 字节码编译器。
> 生成可由 OCaml 解释器运行的可执行文件。
> 更多信息：<https://ocaml.org>。

- 从源文件创建可执行文件：

`ocamlc {{path/to/source_file.ml}}`

- 从源文件创建命名的可执行文件：

`ocamlc -o {{path/to/binary}} {{path/to/source_file.ml}}`

- 自动生成模块签名（接口）文件：

`ocamlc -i {{path/to/source_file.ml}}`