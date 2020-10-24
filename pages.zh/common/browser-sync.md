# browser-sync

> 启动一个本地的服务，可以监听文件改动，刷新浏览器.
> 详见: <https://browsersync.io/docs/command-line>.

- 将指定目录发成服务:

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- 启动当前目录服务，同时监听指定目录下css文件的变动

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- 创建配置文件:

`browser-sync init`

- 按指定配置文件中的配置启动服务:

`browser-sync start --config {{config_file}}`
