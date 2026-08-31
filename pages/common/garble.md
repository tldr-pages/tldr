# garble

> Obfuscate Go builds by stripping information and renaming symbols.
> More information: <https://github.com/burrowers/garble>.

- Build an obfuscated binary for the package in the current directory:

`garble build`

- Build with obfuscated literals such as strings and numbers:

`garble -literals build`

- Build a stripped and minimized binary for extra obfuscation:

`garble -tiny build`

- Build an obfuscated binary with a custom seed for reproducible builds:

`garble -seed={{seed}} build`

- Run tests with obfuscated packages:

`garble test`

- De-obfuscate a stack trace from an obfuscated binary:

`garble reverse < {{path/to/stack_trace.txt}}`
