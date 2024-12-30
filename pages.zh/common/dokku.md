# dokku

> 基于 Docker 的迷你 Heroku（PaaS）。
> 使用单个 `git-push` 命令轻松将多个应用程序部署到您的服务器，支持不同语言。
> 更多信息：<https://github.com/dokku/dokku>。

- 列出运行中的应用：

`dokku apps`

- 创建一个应用：

`dokku apps:create {{app_name}}`

- 删除一个应用：

`dokku apps:destroy {{app_name}}`

- 安装插件：

`dokku plugin:install {{full_repo_url}}`

- 将数据库链接到应用：

`dokku {{db}}:link {{db_name}} {{app_name}}`