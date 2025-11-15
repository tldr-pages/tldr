# brew list

> 列出已安装的软件包/安装包，或者它们所含的文件。
> 更多信息：<https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- 列出所有安装的软件包和安装包：

`brew list`

- 列出属于已安装软件包的文件：

`brew list {{软件包}}`

- 列出安装包的所含文件：

`brew list {{安装包}}`

- 仅列出软件包：

`brew list --formula`

- 仅列出安装包：

`brew list --cask`

- 仅列出锁定的软件包：

`brew list --pinned`
