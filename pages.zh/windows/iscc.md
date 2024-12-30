# iscc

> Inno Setup 安装程序的编译器。
> 它将 Inno Setup 脚本编译成 Windows 安装程序可执行文件。
> 更多信息：<https://jrsoftware.org/isinfo.php>。

- 编译 Inno Setup 脚本：

`iscc {{path\to\file.iss}}`

- 安静地编译 Inno Setup 安装程序：

`iscc /Q {{path\to\file.iss}}`

- 编译签名的 Inno Setup 安装程序：

`iscc /S={{name}}={{command}} {{path\to\file.iss}}`