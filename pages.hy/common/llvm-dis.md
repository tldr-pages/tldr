# llvm-dis

> Փոխակերպեք LLVM բիթկոդի ֆայլերը մարդու կողմից ընթեռնելի LLVM միջանկյալ ներկայացուցչության (IR):.
> Լրացուցիչ տեղեկություններ. <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>:.

- Փոխակերպեք բիթկոդի ֆայլը որպես LLVM IR և արդյունքը գրեք `stdout`:

`llvm-dis {{path/to/input.bc}} -o -`

- Փոխարկեք բիթկոդ ֆայլը LLVM IR ֆայլի նույն ֆայլի անունով.:

`llvm-dis {{path/to/file.bc}}`

- Փոխակերպեք բիթկոդի ֆայլը LLVM IR՝ արդյունքը գրելով նշված ֆայլին.:

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`
