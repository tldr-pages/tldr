# vswhere

> 用于查找 Visual Studio 2017 及更高版本的安装位置。
> 更多信息：<https://github.com/microsoft/vswhere>。

- 查找设置环境变量的 `vcvarsall.bat` 路径：

`vswhere -products * -latest -prerelease -find **\VC\Auxiliary\Build\vcvarsall.bat`

- 查找 x64 MSVC 编译器（如 `cl.exe` 等）的目录：

`vswhere -products * -latest -prerelease -find **\Hostx64\x64\*`

- 查找随 Visual Studio 捆绑的 Clang（如 `clang-cl`、`clang-tidy` 等）的目录：

`vswhere -products * -latest -prerelease -find **\Llvm\bin\*`

- 查找 `MSBuild.exe` 的路径：

`vswhere -products * -latest -prerelease -find MSBuild\**\Bin\MSBuild.exe`