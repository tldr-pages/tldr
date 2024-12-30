# tlmgr 移除

> 卸载 TeX Live 包。
> 默认情况下，已移除的包将备份到 TL 安装目录下的 `./tlpkg/backups`。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 卸载一个 TeX Live 包：

`sudo tlmgr remove {{package}}`

- 模拟卸载一个包而不进行任何更改：

`tlmgr remove --dry-run {{package}}`

- 卸载一个包而不卸载其依赖项：

`sudo tlmgr remove --no-depends {{package}}`

- 卸载一个包并将其备份到特定目录：

`sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}`

- 卸载所有 TeX Live，并请求确认：

`sudo tlmgr remove --all`