# cpan

> 从 CPAN 站点查询、下载和构建 Perl 模块。
> 更多信息：<https://manned.org/cpan>.

- 安装一个模块（`-i` 是可选的）：

`cpan {{-i}} {{module_name}}`

- 强制安装一个模块（`-i` 是必需的）：

`cpan -fi {{module_name}}`

- 升级所有已安装的模块：

`cpan -u`

- 重新编译模块：

`cpan -r`