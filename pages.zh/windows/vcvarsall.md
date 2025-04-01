# vcvarsall

> 设置使用 Microsoft Visual Studio 工具所需的环境变量。
> 某个 Visual Studio 安装的 `vcvarsall` 路径可以使用 `vswhere` 找到。
> 更多信息：<https://learn.microsoft.com/cpp/build/building-on-the-command-line>。

- 设置本地 x64 环境：

`vcvarsall x64`

- 从 x64 主机设置交叉编译本地 x86 环境：

`vcvarsall x64_x86`

- 从 x64 主机设置交叉编译本地 Arm x64 环境：

`vcvarsall x64_arm64`

- 设置本地 UWP x64 环境：

`vcvarsall x64 uwp`