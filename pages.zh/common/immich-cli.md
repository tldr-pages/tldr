# immich-cli

> Immich 提供了一个命令行界面 (CLI)，允许你从命令行执行某些操作。
> 另请参见：`immich-go`。
> 更多信息：<https://immich.app/docs/features/command-line-interface/>。

- 登录到 Immich 服务器：

`immich login {{server_url/api}} {{server_key}}`

- 上传一些图像文件：

`immich upload {{file1.jpg file2.jpg}}`

- 上传包含子目录的目录：

`immich upload --recursive {{path/to/directory}}`

- 根据目录创建相册：

`immich upload --album-name "{{My summer holiday}}" --recursive {{path/to/directory}}`

- 跳过匹配通配符模式的资产：

`immich upload --ignore {{**/Raw/** **/*.tif}} --recursive {{path/to/directory}}`

- 包括隐藏文件：

`immich upload --include-hidden --recursive {{path/to/directory}}`