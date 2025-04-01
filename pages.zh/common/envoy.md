# envoy

> 基于 PHP 的 Laravel 远程服务器任务管理器。
> 更多信息：<https://laravel.com/docs/envoy>.

- 初始化配置文件：

`envoy init {{host_name}}`

- 运行任务：

`envoy run {{task_name}}`

- 从特定项目中运行任务：

`envoy run --path {{path/to/directory}} {{task_name}}`

- 运行任务并在失败时继续：

`envoy run --continue {{task_name}}`

- 将任务导出为 Bash 脚本以便检查：

`envoy run --pretend {{task_name}}`

- 通过 SSH 连接到指定服务器：

`envoy ssh {{server_name}}`