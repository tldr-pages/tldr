# fswatch

> 一个跨平台的文件变更监控工具。
> 更多信息： <https://emcrisostomo.github.io/fswatch>.

- 在文件创建、更新或删除时运行 Bash 命令：

`fswatch {{path/to/file}} | xargs -n 1 {{bash_command}}`

- 监视一个或多个文件和/或目录：

`fswatch {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs -n 1 {{bash_command}}`

- 打印变更文件的绝对路径：

`fswatch {{path/to/directory}} | xargs -n 1 -I {} echo {}`

- 按事件类型过滤：

`fswatch --event {{Updated|Removed|Created|...}} {{path/to/directory}} | xargs -n 1 {{bash_command}}`