# wapm

> WebAssembly 包管理器。
> 更多信息：<https://wapm.io/help/reference>。

- 交互式创建新的 `wapm.toml` 文件：

`wapm init`

- 下载 `wapm.toml` 中列出的所有依赖包：

`wapm install`

- 下载指定版本的包并将其添加到 `wapm.toml` 的依赖列表中：

`wapm install {{package}}@{{version}}`

- 下载并全局安装一个包：

`wapm install --global {{package}}`

- 卸载一个包并将其从 `wapm.toml` 的依赖列表中移除：

`wapm uninstall {{package}}`

- 打印本地安装的依赖包树：

`wapm list`

- 列出顶级全局安装的包：

`wapm list --global`

- 使用 Wasmer 运行时执行包命令：

`wapm run {{command_name}} {{arguments}}`
