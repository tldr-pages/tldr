# vswhere

> 查找 Visual Studio 2017 及更高版本的安装。
> 更多信息：<https://github.com/microsoft/vswhere>。

- 查找 vcvarsall.bat 的路径以设置环境变量：

`vswhere -products * -latest -prerelease -find **\VC\Auxiliary\Build\vcvarsall.bat`

- 查找 x64 MSVC 编译器（cl.exe 等）的目录：

`vswhere -products * -latest -prerelease -find **\Hostx64\x64\*`

- 查找与 Visual Studio 一起捆绑的 Clang（clang-cl、clang-tidy 等）的目录：

`vswhere -products * -latest -prerelease -find **\Llvm\bin\*`

- 查找 `MSBuild.exe` 的路径：

`vswhere -products * -latest -prerelease -find MSBuild\**\Bin\MSBuild.exe`