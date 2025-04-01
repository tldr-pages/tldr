# tlmgr option

> TeX Live 设置管理器。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有 TeX Live 设置：

`tlmgr option showall`

- 列出当前所有已设置的 TeX Live 设置：

`tlmgr option show`

- 以 JSON 格式打印所有 TeX Live 设置：

`tlmgr option showall --json`

- 显示特定 TeX Live 设置的值：

`tlmgr option {{setting}}`

- 修改特定 TeX Live 设置的值：

`tlmgr option {{setting}} {{value}}`

- 安装后从 DVD 设置 TeX Live 从互联网获取未来更新：

`tlmgr option {{repository}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`