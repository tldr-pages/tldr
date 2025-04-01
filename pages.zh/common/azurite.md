# azurite

> 适用于本地环境的 Azure Storage API 兼容服务器（仿真器）。
> 更多信息：<https://www.npmjs.com/package/azurite>。

- 使用现有的位置作为工作区路径：

`azurite {{[-l|--location]}} {{path/to/directory}}`

- 禁用控制台中显示的访问日志：

`azurite {{[-s|--silent]}}`

- 通过提供日志文件路径启用调试日志：

`azurite {{[-d|--debug]}} {{path/to/debug.log}}`

- 自定义 Blob/Queue/Table 服务的监听地址：

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- 自定义 Blob/Queue/Table 服务的监听端口：

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`