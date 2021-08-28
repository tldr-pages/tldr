# adscript

> Compiler for Adscript files.
> More information: <https://github.com/Amplus2/Adscript>.

- Compile a file to an object file:

`adscript --output {{path/to/program.o}} {{path/to/program.adscript}}`

- Compile and link a file to a standalone executable:

`adscript --executable --output {{path/to/program}} {{path/to/program.adscript}}`

- Compile a file to LLVM IR instead of native machine code:

`adscript --llvm-ir --output {{path/to/program.ll}} {{path/to/program.adscript}}`

- Cross-compile a file to an object file for a foreign CPU architecture or operating system:

`adscript --target-triple {{i386-linux-elf}} --output {{path/to/program.o}} {{path/to/program.adscript}}`
