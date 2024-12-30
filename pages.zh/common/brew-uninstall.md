# brew 卸载

> 卸载 Homebrew 配方/软件包。
> 使用 `brew autoremove` 来移除不再使用的依赖项。
> 更多信息：<https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->。

- 卸载一个配方/软件包：

`brew uninstall {{配方|软件包}}`

- 卸载一个软件包并删除所有相关文件：

`brew uninstall --zap {{软件包}}`