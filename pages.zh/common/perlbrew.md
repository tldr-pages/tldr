# perlbrew

> 在家目录中管理 Perl 安装。
> 参见：`asdf`。
> 更多信息：<https://github.com/gugod/App-perlbrew>。

- 初始化 `perlbrew` 环境：

`perlbrew init`

- 列出可用的 Perl 版本：

`perlbrew available`

- 安装/卸载 Perl 版本：

`perlbrew {{install|uninstall}} {{version}}`

- 列出 Perl 安装：

`perlbrew list`

- 切换到一个安装并将其设置为默认：

`perlbrew switch perl-{{version}}`

- 再次使用系统 Perl：

`perlbrew off`

- 列出当前使用安装的已安装 CPAN 模块：

`perlbrew list-modules`

- 从一个安装克隆 CPAN 模块到另一个安装：

`perlbrew clone-modules {{source_installation}} {{destination_installation}}`
