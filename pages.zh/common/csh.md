# csh

> 使用类似C语言语法的命令行解释器（shell）。
> 另见：`tcsh`。
> 更多信息：<https://www.mkssoftware.com/docs/man1/csh.1.asp>。

- 启动交互式shell会话：

`csh`

- 启动不加载启动配置的交互式shell会话：

`csh -f`

- 执行特定的[c]ommands：

`csh -c "{{echo 'csh 被执行'}}"`

- 执行特定脚本：

`csh {{path/to/script.csh}}`