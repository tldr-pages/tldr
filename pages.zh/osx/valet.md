# valet

> 一个 Laravel 开发环境，允许通过本地隧道 `http://<example>.test` 来托管站点。
> 更多信息：<https://laravel.com/docs/valet>.

- 启动 valet 守护进程：

`valet start`

- 将当前工作目录注册为 Valet 应搜索的站点路径：

`valet park`

- 查看已“停放”的路径：

`valet paths`

- 为单个站点提供服务，而不是整个目录：

`valet link {{application_name}}`

- 通过 Ngrok 隧道分享项目：

`valet share`