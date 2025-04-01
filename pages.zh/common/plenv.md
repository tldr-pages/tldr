# plenv

> 在多个 Perl 版本之间切换。
> 更多信息：<https://github.com/tokuhirom/plenv>。

- 显示当前选定的 Perl 版本及其选择方式：

`plenv version`

- 列出所有已安装的 Perl 版本：

`plenv versions`

- 设置全局 Perl 版本（除非设置了本地或 Shell 版本，否则使用此版本）：

`plenv global {{version}}`

- 设置本地应用程序特定的 Perl 版本（在当前目录及其所有子目录中使用）：

`plenv local {{version}}`

- 设置特定于 Shell 的 Perl 版本（仅在当前会话中使用）：

`plenv shell {{version}}`

- 显示帮助信息：

`plenv`

- 显示特定命令的帮助信息：

`plenv help {{command}}`