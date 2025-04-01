# fdroidcl

> 管理通过 ADB 连接的设备上的 F-Droid 应用。
> 更多信息：<https://github.com/mvdan/fdroidcl>.

- 获取 F-Droid 索引：

`fdroidcl update`

- 显示应用的信息：

`fdroidcl show {{app_id}}`

- 下载应用的 APK 文件：

`fdroidcl download {{app_id}}`

- 在索引中搜索应用：

`fdroidcl search {{search_pattern}}`

- 在连接的设备上安装应用：

`fdroidcl install {{app_id}}`

- 添加仓库：

`fdroidcl repo add {{repo_name}} {{url}}`

- 移除、启用或禁用仓库：

`fdroidcl repo {{remove|enable|disable}} {{repo_name}}`
