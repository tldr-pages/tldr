# puppet apply

> 本地应用 Puppet 清单。
> 更多信息： <https://puppet.com/docs/puppet/7/man/apply.html>。

- 应用清单：

`puppet apply {{path/to/manifest}}`

- 执行 Puppet 代码：

`puppet apply --execute {{code}}`

- 使用特定的模块和 hiera 配置文件：

`puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}`
