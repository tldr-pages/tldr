# tlmgr remove

> 卸载 TeX Live 软件包。
> 默认情况下，已移除的软件包将备份到 TL 安装目录下的 `./tlpkg/backups`。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 卸载 TeX Live 软件包：

`sudo tlmgr remove {{package}}`

- 模拟卸载软件包，但不进行实际更改：

`tlmgr remove --dry-run {{package}}`

- 卸载软件包但不卸载其依赖项：

`sudo tlmgr remove --no-depends {{package}}`

- 卸载软件包并备份到指定目录：

`sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}`

- 卸载所有 TeX Live 软件包，并请求确认：

`sudo tlmgr remove --all`
