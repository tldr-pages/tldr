# iscc

> Inno Setup 安装程序的编译器。
> 它将 Inno Setup 脚本编译为 Windows 安装程序可执行文件。
> 更多信息：<https://jrsoftware.org/isinfo.php>.

- 编译一个 Inno Setup 脚本：

`iscc {{脚本路径.iss}}`

- 静默编译一个 Inno Setup 安装程序：

`iscc /Q {{脚本路径.iss}}`

- 编译已签名的 Inno Setup 安装程序：

`iscc /S={{名称}}={{命令}} {{脚本路径.iss}}`
