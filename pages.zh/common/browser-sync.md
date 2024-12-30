# browser-sync

> 一个在文件更改时更新浏览器的本地网络服务器。
> 更多信息：<https://browsersync.io/docs/command-line>。

- 从指定目录启动服务器：

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- 从本地目录启动服务器，监视目录中的所有 CSS 文件：

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- 创建配置文件：

`browser-sync init`

- 从配置文件启动 Browsersync：

`browser-sync start --config {{config_file}}`