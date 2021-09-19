# llvm-bcanalyzer

> LLVM Bitcode (`.bc`) analyzer.
> More information: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Print statistics on a Bitcode file:

`llvm-bcanalyzer {{path/to/file.bc}}`

- Print an SGML representation of and statistics on a Bitcode file:

`llvm-bcanalyzer -dump {{path/to/file.bc}}`

- Read a Bitcode file from `stdin` and analyze it:

`cat {{path/to/file.bc}} | llvm-bcanalyzer`
