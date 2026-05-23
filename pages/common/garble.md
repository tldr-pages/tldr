# garble

> Obfuscate Go builds by wrapping the Go toolchain.
> More information: <https://github.com/burrowers/garble>.

- Build an obfuscated program:

`garble build {{./cmd/program}}`

- Build an obfuscated program with a specific output filename:

`garble build -o {{path/to/binary}} {{./cmd/program}}`

- Build with literal obfuscation enabled:

`garble -literals build {{./cmd/program}}`

- Build a smaller obfuscated binary by stripping extra runtime information:

`garble -tiny build {{./cmd/program}}`

- Run tests with obfuscated code:

`garble test {{./...}}`

- Run an obfuscated program:

`garble run {{./cmd/program}}`
