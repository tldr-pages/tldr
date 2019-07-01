# iscc

> Inno Setup安装程序的编译器.
> 它将Inno Setup脚本编译为Windows安装程序可执行文件.

- 编译一个Inno Setup脚本:

`iscc {{脚本路径.iss}}`

- 静默编译一个Inno Setup安装程序:

`iscc /Q {{脚本路径.iss}}`

- 编译已签名的Inno Setup安装程序:

`iscc /S={{名称}}={{命令}} {{脚本路径.iss}}`
