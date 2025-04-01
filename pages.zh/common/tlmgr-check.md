# tlmgr check

> 检查 TeX Live 安装的一致性。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 检查整个 TeX Live 安装的一致性：

`tlmgr check all`

- 以详细模式检查整个 TeX Live 信息的一致性：

`tlmgr check all -v`

- 检查缺失的依赖项：

`tlmgr check depends`

- 检查所有 TeX Live 可执行文件是否都在：

`tlmgr check executes`

- 检查本地 TLPDB 中列出的所有文件是否都在：

`tlmgr check files`

- 检查运行文件部分中是否有重复的文件名：

`tlmgr check runfiles`