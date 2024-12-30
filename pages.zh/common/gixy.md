# gixy

> 分析 nginx 配置文件。
> 更多信息：<https://github.com/yandex/gixy>。

- 分析 nginx 配置（默认路径：`/etc/nginx/nginx.conf`）：

`gixy`

- 分析 nginx 配置，但跳过特定测试：

`gixy --skips {{http_splitting}}`

- 以特定严重性级别分析 nginx 配置：

`gixy {{-l|-ll|-lll}}`

- 在特定路径分析 nginx 配置文件：

`gixy {{path/to/configuration_file_1}} {{path/to/configuration_file_2}}`