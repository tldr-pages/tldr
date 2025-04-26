# luac

> Lua bytecode compiler.
> More information: <https://www.lua.org/manual/5.4/luac.html>.

- Compile a Lua source file to Lua bytecode:

`luac -o {{byte_code.luac}} {{source.lua}}`

- Do not include debug symbols in the output:

`luac -s -o {{byte_code.luac}} {{source.lua}}`
