# web-ext

> 一个用于管理网络扩展开发的命令行工具。
> 更多信息请访问：<https://github.com/mozilla/web-ext>。

- 在当前目录中以 Firefox 运行网络扩展：

`web-ext run`

- 从特定目录在 Firefox 中运行网络扩展：

`web-ext run --source-dir {{path/to/directory}}`

- 显示详细的执行输出：

`web-ext run --verbose`

- 在 Firefox Android 中运行网络扩展：

`web-ext run --target firefox-android`

- 检查清单和源文件中的错误：

`web-ext lint`

- 构建和打包扩展：

`web-ext build`

- 显示详细的构建输出：

`web-ext build --verbose`

- 为自托管签名一个包：

`web-ext sign --api-key {{api_key}} --api-secret {{api_secret}}`