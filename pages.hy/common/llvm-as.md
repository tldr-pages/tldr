# llvm-as

> LLVM միջանկյալ ներկայացում (`.ll`) Bitcode (`.bc`) assembler-ում:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/llvm-as.html>:.

- Հավաքեք IR ֆայլ.:

`llvm-as -o {{path/to/out.bc}} {{path/to/source.ll}}`

- Հավաքեք IR ֆայլ և ներառեք մոդուլի հեշը արտադրված Bitcode ֆայլում.:

`llvm-as --module-hash -o {{path/to/out.bc}} {{path/to/source.ll}}`

- Կարդացեք IR ֆայլ `stdin`-ից և հավաքեք այն.:

`cat {{path/to/source.ll}} | llvm-as -o {{path/to/out.bc}}`
