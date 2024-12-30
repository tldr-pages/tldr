# xonsh

> 基于 Python 的跨平台 Unix 风格的 shell。
> 在 Xonsh 中编写和混合 sh/Python 代码（发音为 conch）。
> 更多信息：<https://xon.sh>。

- 开始一个交互式 shell 会话：

`xonsh`

- 执行单个命令然后退出：

`xonsh -c "{{command}}"`

- 从脚本文件中运行命令然后退出：

`xonsh {{path/to/script_file.xonsh}}`

- 为 shell 进程定义环境变量：

`xonsh -D{{name1}}={{value1}} -D{{name2}}={{value2}}`

- 加载指定的 `.xonsh` 或 `.json` 配置文件：

`xonsh --rc {{path/to/file1.xonsh}} {{path/to/file2.json}}`

- 跳过加载 `.xonshrc` 配置文件：

`xonsh --no-rc`