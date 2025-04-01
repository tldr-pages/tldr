# brew list

> 列出已安装的软件包或其文件。
> 更多信息：<https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- 列出所有已安装的软件包和 Cask 应用程序：

`brew list`

- 列出属于已安装软件包的文件：

`brew list {{formula}}`

- 列出 Cask 应用程序的文件：

`brew list {{cask}}`

- 仅列出软件包：

`brew list --formula`

- 仅列出 Cask 应用程序：

`brew list --cask`

- 仅列出已固定的软件包：

`brew list --pinned`