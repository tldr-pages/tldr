# luac

> Lua 字节码编译器。
> 更多信息：<https://www.lua.org>。

- 将 Lua 源文件编译为 Lua 字节码：

`luac -o {{byte_code.luac}} {{source.lua}}`

- 在输出中不包含调试符号：

`luac -s -o {{byte_code.luac}} {{source.lua}}`