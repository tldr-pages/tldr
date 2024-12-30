# vcvarsall

> 设置使用 Microsoft Visual Studio 工具所需的环境变量。
> 可以使用 `vswhere` 查找特定 Visual Studio 安装的 `vcvarsall` 路径。
> 更多信息：<https://learn.microsoft.com/cpp/build/building-on-the-command-line>。

- 为本机 x64 设置环境：

`vcvarsall x64`

- 为从 x64 主机交叉编译的本机 x86 设置环境：

`vcvarsall x64_x86`

- 为从 x64 主机交叉编译的本机 Arm x64 设置环境：

`vcvarsall x64_arm64`

- 为本机 UWP x64 设置环境：

`vcvarsall x64 uwp`