# Doppler 运行

> 在环境中注入 Doppler 秘密后运行命令。
> 更多信息：<https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>。

- 运行一个命令：

`doppler run --command {{command}}`

- 运行多个命令：

`doppler run --command {{command1 && command2}}`

- 运行一个脚本：

`doppler run {{path/to/command.sh}}`

- 以指定的项目和配置运行命令：

`doppler run -p {{project_name}} -c {{config_name}} -- {{command}}`

- 在秘密更改时自动重启进程：

`doppler run --watch {{command}}`