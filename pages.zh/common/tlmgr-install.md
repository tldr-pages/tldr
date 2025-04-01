# tlmgr install

> 安装 TeX Live 包。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>.

- 安装一个包及其依赖项：

`sudo tlmgr install {{package}}`

- 重新安装一个包：

`sudo tlmgr install --reinstall {{package}}`

- 模拟安装一个包而不进行实际更改：

`tlmgr install --dry-run {{package}}`

- 安装一个包但不安装其依赖项：

`sudo tlmgr install --no-depends {{package}}`

- 从特定文件安装一个包：

`sudo tlmgr install --file {{path/to/package}}`