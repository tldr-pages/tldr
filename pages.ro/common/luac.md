# luac

> compilator de bytecode Lua.
> Mai multe informaţii: <https://www.lua.org>

- Compilarea unui fișier sursă Lua la bytecode Lua:

`luac -o {{byte_code.luac}} {{source.lua}}`

- Nu includeți simbolurile de depanare în ieșire:

`luac -s -o {{byte_code.luac}} {{source.lua}}`
