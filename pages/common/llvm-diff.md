# llvm-diff

> Compare the structure of two LLVM modules.
> More information: <https://llvm.org/docs/CommandGuide/llvm-diff.html>.

- Compare two LLVM assembly files:

`llvm-diff {{path/to/file1.ll}} {{path/to/file2.ll}}`

- Compare two LLVM bitcode files:

`llvm-diff {{path/to/file1.bc}} {{path/to/file2.bc}}`

- Compare specific functions between two modules:

`llvm-diff {{path/to/file1.ll}} {{path/to/file2.ll}} --function={{function_name}}`

- Compare all global values between two modules:

`llvm-diff {{path/to/file1.ll}} {{path/to/file2.ll}} --globals`

- Display help:

`llvm-diff --help`
