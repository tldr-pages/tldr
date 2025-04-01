# tcsh

> 支持文件名补全和命令行编辑的 C shell。
> 请参阅：`csh`。
> 更多信息：<https://manned.org/tcsh>。

- 启动交互式 shell 会话：

`tcsh`

- 不加载启动配置启动交互式 shell 会话：

`tcsh -f`

- 执行特定的 [c]ommands：

`tcsh -c "{{echo 'tcsh is executed'}}"`

- 执行特定的脚本：

`tcsh {{path/to/script.tcsh}}`

- 检查特定脚本的语法错误：

`tcsh -n {{path/to/script.tcsh}}`

- 从 `stdin` 执行特定命令：

`{{echo "echo 'tcsh is executed'"}} | tcsh`