# luac

> Lua bytecode compiler.

- Compile Lua source file to Lua bytecode:

`luac -o {{byte_code.luac}} {{source.lua}}`

- Don't include a debug information in the output:

`luac -s -o {{byte_code.luac}} {{source.lua}}`
