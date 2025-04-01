# kool

> 构建软件开发环境。
> 更多信息：<https://kool.dev/docs/>.

- 使用特定预设创建项目：

`kool create {{preset}} {{project_name}}`

- 运行当前目录中 `kool.yml` 文件中定义的特定脚本：

`kool run {{script}}`

- 启动/停止当前目录中的服务：

`kool {{start|stop}}`

- 显示当前目录中服务的状态：

`kool status`

- 更新到最新版本：

`kool self-update`

- 打印指定 shell 的补全脚本：

`kool completion {{bash|fish|powershell|zsh}}`