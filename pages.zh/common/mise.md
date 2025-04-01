# mise

> 管理不同包的版本。
> 更多信息：<https://mise.jdx.dev>.

- 列出所有可用的插件：

`mise plugins list-all`

- 安装插件：

`mise plugins add {{name}}`

- 列出可用于安装的运行时版本：

`mise ls-remote {{name}}`

- 安装特定版本的包：

`mise install {{name}}@{{version}}`

- 设置包的全局版本：

`mise use --global {{name}}@{{version}}`

- 设置包的本地版本：

`mise use {{name}}@{{version}}`

- 在配置中设置环境变量：

`mise set {{variable}}={{value}}`