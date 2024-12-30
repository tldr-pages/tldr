# zig

> Zig 编译器和工具链。
> 更多信息：<https://ziglang.org>。

- 在当前目录中编译项目：

`zig build`

- 编译并运行当前目录中的项目：

`zig build run`

- 初始化一个包含库和可执行文件的 `zig build` 项目：

`zig init`

- 创建并运行测试构建：

`zig test {{path/to/file.zig}}`

- 为 `x86_64` 架构和 `windows` 操作系统交叉编译、构建并运行项目：

`zig build run -fwine -Dtarget=x86_64-windows`

- 将 Zig 源代码格式化为规范形式：

`zig fmt {{path/to/file.zig}}`

- 将 C 文件转换为 `zig`：

`zig translate-c -lc {{path/to/file.c}}`

- 将 Zig 作为替代 C++ 编译器使用：

`zig c++ {{path/to/file.cpp}}`