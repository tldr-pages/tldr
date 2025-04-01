# gixy

> 分析 Nginx 配置文件。
> 更多信息：<https://github.com/yandex/gixy>。

- 分析 Nginx 配置文件（默认路径：`/etc/nginx/nginx.conf`）：

`gixy`

- 分析 Nginx 配置文件但跳过特定测试：

`gixy --skips {{http_splitting}}`

- 使用特定严重性级别分析 Nginx 配置文件：

`gixy {{-l|-ll|-lll}}`

- 分析特定路径上的 Nginx 配置文件：

`gixy {{path/to/configuration_file_1}} {{path/to/configuration_file_2}}`
