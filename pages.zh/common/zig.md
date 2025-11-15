# zig

> Zig 编译器和工具链。
> 更多信息：<https://ziglang.org/documentation/master/>.

- 编译当前目录下的项目：

`zig build`

- 编译并运行当前目录下的项目：

`zig build run`

- 初始化一个 `zig build` 应用程序：

`zig init-exe`

- 初始化一个 `zig build` 库：

`zig init-lib`

- 创建并运行一个测试构建：

`zig test {{路径/到/文件.zig}}`

- 将 Zig 源码重新格式化为规范格式：

`zig fmt {{路径/到/文件.zig}}`

- 将 Zig 用作 C 编译器：

`zig cc {{路径/到/文件.c}}`

- 将 Zig 用作 C++ 编译器：

`zig c++ {{路径/到/文件.cpp}}`
