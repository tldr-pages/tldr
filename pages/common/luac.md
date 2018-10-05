# luac

> Lua byte code compiler.

- Compile a lua source code to a lua byte code:

`luac -o {{byte_code.luac}} {{source.lua}}`

- Don't include a debug information in the byte code:

`luac -s -o {{byte_code.luac}} {{source.lua}}`
