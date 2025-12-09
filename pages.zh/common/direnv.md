# direnv

> Shell 扩展为加载和卸载环境变量，具体取决于当前目录。
> 更多信息：<https://github.com/direnv/direnv>.

- 授予 direnv 当前目录中加载 `.envrc`:

`direnv allow {{.}}`

- 撤销在当前目录加载 `.envrc` 的授权：

`direnv deny {{.}}`

- 使用默认编辑器编辑 `.envrc` 并在退出时重载环境：

`direnv edit {{.}}`

- 触发环境重载：

`direnv reload`

- 打印一些调试状态信息：

`direnv status`
