# tlmgr 纸张

> 管理 TeX Live 安装的纸张大小选项。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 显示所有 TeX Live 程序使用的默认纸张大小：

`tlmgr paper`

- 将所有 TeX Live 程序的默认纸张大小设置为 A4：

`sudo tlmgr paper {{a4}}`

- 显示特定 TeX Live 程序使用的默认纸张大小：

`tlmgr {{pdftex}} paper`

- 将特定 TeX Live 程序的默认纸张大小设置为 A4：

`sudo tlmgr {{pdftex}} paper {{a4}}`

- 列出特定 TeX Live 程序可用的所有纸张大小：

`tlmgr {{pdftex}} paper --list`

- 以 JSON 格式输出所有 TeX Live 程序使用的默认纸张大小：

`tlmgr paper --json`