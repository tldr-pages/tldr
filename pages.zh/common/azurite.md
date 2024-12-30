# azurite

> Azure 存储 API 兼容的服务器（模拟器），用于本地环境。
> 更多信息：<https://www.npmjs.com/package/azurite>。

- 使用现有位置作为工作区路径：

`azurite {{-l|--location}} {{path/to/directory}}`

- 禁用在控制台中显示的访问日志：

`azurite {{-s|--silent}}`

- 通过提供文件路径作为日志目标来启用调试日志：

`azurite {{-d|--debug}} {{path/to/debug.log}}`

- 自定义 Blob/队列/表服务的监听地址：

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- 自定义 Blob/队列/表服务的监听端口：

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`