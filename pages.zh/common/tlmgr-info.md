# tlmgr 信息

> 显示 TeX Live 包的信息。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有可用的 TeX Live 包，已安装的包前缀为 `i`：

`tlmgr info`

- 列出所有可用的集合：

`tlmgr info collections`

- 列出所有可用的方案：

`tlmgr info scheme`

- 显示特定包的信息：

`tlmgr info {{package}}`

- 列出特定包中包含的所有文件：

`tlmgr info {{package}} --list`

- 列出所有已安装的包：

`tlmgr info --only-installed`

- 仅显示特定包的信息：

`tlmgr info {{package}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},..."`

- 将所有可用的包以 JSON 编码数组的形式打印：

`tlmgr info --json`