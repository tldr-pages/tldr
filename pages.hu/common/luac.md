# luac

> Lua bytecode fordító. További információ: <https://www.lua.org>.

- Egy Lua forrásfájl Lua bytecode-ba fordítása:

`luac -o {{byte_code.luac}} {{source.lua}}`

- Ne tartalmazzon hibakereső szimbólumokat a kimeneten:

`luac -s -o {{byte_code.luac}} {{source.lua}}`
