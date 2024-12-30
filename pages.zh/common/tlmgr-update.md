# tlmgr 更新

> 更新 TeX Live 包。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 更新所有 TeX Live 包：

`sudo tlmgr update --all`

- 更新 tlmgr 本身：

`sudo tlmgr update --self`

- 更新特定包：

`sudo tlmgr update {{package}}`

- 更新所有包，排除特定包：

`sudo tlmgr update --all --exclude {{package}}`

- 更新所有包，并备份当前包：

`sudo tlmgr update --all --backup`

- 更新特定包，但不更新其依赖：

`sudo tlmgr update --no-depends {{package}}`

- 模拟更新所有包而不做任何更改：

`sudo tlmgr update --all --dry-run`