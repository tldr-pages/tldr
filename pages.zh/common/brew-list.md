# brew list

> 列出已安装的配方/软件包或它们的文件。
> 更多信息：<https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->。

- 列出所有已安装的配方和软件包：

`brew list`

- 列出属于已安装配方的文件：

`brew list {{formula}}`

- 列出软件包的工件：

`brew list {{cask}}`

- 仅列出配方：

`brew list --formula`

- 仅列出软件包：

`brew list --cask`

- 仅列出已固定的配方：

`brew list --pinned`