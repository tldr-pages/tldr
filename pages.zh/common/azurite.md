# azurite

> 在本地环境中运行的、与 Azure Storage API 兼容的服务器（模拟器）。
> 更多信息：<https://www.npmjs.com/package/azurite>.

- 使用已有的位置作为工作区路径：

`azurite {{[-l|--location]}} {{路径/到/目录}}`

- 禁用在控制台中显示的访问日志：

`azurite {{[-s|--silent]}}`

- 通过提供文件路径作为日志输出位置来启用调试日志：

`azurite {{[-d|--debug]}} {{路径/到/debug.log}}`

- 自定义 Blob / Queue / Table 服务的监听地址：

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- 自定义 Blob / Queue / Table 服务的监听端口：

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`
