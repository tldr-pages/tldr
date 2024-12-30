# fdroid

> F-Droid构建工具。
> F-Droid是一个可安装的FOSS（自由开源软件）应用程序目录，适用于Android平台。
> 更多信息：<https://f-droid.org/>。

- 构建特定应用：

`fdroid build {{app_id}}`

- 在构建服务器虚拟机中构建特定应用：

`fdroid build {{app_id}} --server`

- 将应用发布到本地库：

`fdroid publish {{app_id}}`

- 在每个连接的设备上安装应用：

`fdroid install {{app_id}}`

- 检查元数据格式是否正确：

`fdroid lint --format {{app_id}}`

- 自动修复格式（如果可能）：

`fdroid rewritemeta {{app_id}}`