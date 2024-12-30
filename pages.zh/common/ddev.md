# ddev

> 基于容器的 PHP 环境本地开发工具。
> 更多信息请访问：<https://ddev.readthedocs.io>。

- 启动一个项目：

`ddev start`

- 配置项目类型和文档根目录：

`ddev config`

- [f]ollow 日志记录：

`ddev logs -f`

- 在容器内运行 composer：

`ddev composer`

- 安装特定版本的 Node.js：

`ddev nvm install {{version}}`

- 导出数据库：

`ddev export-db --file={{/tmp/db.sql.gz}}`

- 在容器内运行特定命令：

`ddev exec {{echo 1}}`