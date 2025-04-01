# tlmgr info

> 显示 TeX Live 包的信息。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有可用的 TeX Live 包，已安装的包前面加上 `i`：

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

- 仅显示包的特定信息：

`tlmgr info {{package}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},..."`

- 以 JSON 编码数组形式打印所有可用的包：

`tlmgr info --json`
