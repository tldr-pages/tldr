# ddev

> 基于容器的 PHP 环境本地开发工具。
> 更多信息：<https://ddev.readthedocs.io/en/stable/users/usage/cli/>.

- 启动项目：

`ddev start`

- 配置项目的类型和文档根目录：

`ddev config`

- 跟踪日志：

`ddev logs {{[-f|--follow]}}`

- 在容器内运行 Composer：

`ddev composer`

- 安装特定版本的 Node.js：

`ddev nvm install {{version}}`

- 导出数据库：

`ddev export-db {{[-f|--file]}} {{/tmp/db.sql.gz}}`

- 在容器内运行特定命令：

`ddev exec {{echo 1}}`
