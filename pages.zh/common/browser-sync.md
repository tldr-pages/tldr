# browser-sync

> 启动一个本地的服务，可以监听文件改动，刷新浏览器。
> 更多信息：<https://browsersync.io/docs/command-line>.

- 将指定目录发成服务：

`browser-sync start --server {{路径/到/目录}} --files {{路径/到/目录}}`

- 启动当前目录服务，同时监听指定目录下 `css` 文件的变动：

`browser-sync start --server --files '{{路径/到/目录/*.css}}'`

- 创建配置文件：

`browser-sync init`

- 按指定配置文件中的配置启动服务：

`browser-sync start --config {{配置文件}}`
