# var-dump-server

> Symfony 数据转储服务器。
> 收集由 Symfony VarDumper 组件转储的数据。
> 更多信息：<https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>。

- 启动服务器：

`var-dump-server`

- 将数据转储到 HTML 文件中：

`var-dump-server --format=html > {{path/to/file.html}}`

- 让服务器监听特定的地址和端口：

`var-dump-server --host {{127.0.0.1:9912}}`