# direnv

> 一个Shell扩展，根据当前目录加载和卸载环境变量。
> 更多信息：<https://github.com/direnv/direnv>。

- 授予direnv权限以加载当前目录中的`.envrc`：

`direnv allow {{.}}`

- 撤销加载当前目录中的`.envrc`的授权：

`direnv deny {{.}}`

- 在默认文本编辑器中编辑`.envrc`文件，并在退出时重新加载环境：

`direnv edit {{.}}`

- 触发环境的重新加载：

`direnv reload`

- 打印一些调试状态信息：

`direnv status`