# valet

> 一个Laravel开发环境，允许通过本地隧道在`http://<example>.test`上托管网站。
> 更多信息请访问：<https://laravel.com/docs/valet>。

- 启动valet守护进程：

`valet start`

- 将当前工作目录注册为Valet应搜索的网站路径：

`valet park`

- 查看“停放”的路径：

`valet paths`

- 服务单个网站，而不是整个目录：

`valet link {{application_name}}`

- 通过Ngrok隧道分享项目：

`valet share`