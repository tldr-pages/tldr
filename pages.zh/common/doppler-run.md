# doppler run

> 用 Doppler 密钥注入环境变量执行命令。
> 更多信息：<https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>.

- 执行命令：

`doppler run --command {{command}}`

- 执行多个命令：

`doppler run --command {{command1 && command2}}`

- 执行脚本：

`doppler run {{path/to/command.sh}}`

- 用指定的项目和配置执行命令：

`doppler run -p {{project_name}} -c {{config_name}} -- {{command}}`

- 当密钥变化时自动重启进程：

`doppler run --watch {{command}}`