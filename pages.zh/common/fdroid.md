# fdroid

> F-Droid 构建工具。
> F-Droid 是一个可安装的目录，包含适用于 Android 平台的 FOSS（自由和开源软件）应用程序。
> 更多信息：<https://f-droid.org/>。

- 构建特定应用：

`fdroid build {{app_id}}`

- 在构建服务器 VM 中构建特定应用：

`fdroid build {{app_id}} --server`

- 将应用发布到本地仓库：

`fdroid publish {{app_id}}`

- 在所有已连接的设备上安装应用：

`fdroid install {{app_id}}`

- 检查元数据格式是否正确：

`fdroid lint --format {{app_id}}`

- 自动修复格式（如果可能）：

`fdroid rewritemeta {{app_id}}`