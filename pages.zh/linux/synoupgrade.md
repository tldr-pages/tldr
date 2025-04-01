# synoupgrade

> 升级 Synology DiskStation Manager (DSM) - Synology NAS 操作系统。
> 更多信息：<https://www.synology.com/dsm>。

- 检查是否有可用的升级：

`sudo synoupgrade --check`

- 检查补丁而不升级 DSM 版本：

`sudo synoupgrade --check-smallupdate`

- 下载可用的最新升级（使用 `--download-smallupdate` 以下载补丁）：

`sudo synoupgrade --download`

- 开始升级过程：

`sudo synoupgrade --start`

- 自动升级到最新版本：

`sudo synoupgrade --auto`

- 自动应用补丁而不升级 DSM 版本：

`sudo synoupgrade --auto-smallupdate`

- 使用补丁文件升级 DSM（应为绝对路径）：

`sudo synoupgrade --patch {{/path/to/file.pat}}`

- 显示帮助：

`synoupgrade`