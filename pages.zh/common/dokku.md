# dokku

> 基于 Docker 的 mini-Heroku（PaaS）。
> 使用单个 `git-push` 命令轻松将多种语言的应用部署到服务器。
> 更多信息：<https://github.com/dokku/dokku>。

- 列出正在运行的应用：

`dokku apps`

- 创建应用：

`dokku apps:create {{app_name}}`

- 删除应用：

`dokku apps:destroy {{app_name}}`

- 安装插件：

`dokku plugin:install {{full_repo_url}}`

- 将数据库链接到应用：

`dokku {{db}}:link {{db_name}} {{app_name}}`
