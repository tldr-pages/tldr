# heroku

> 从命令行创建和管理 Heroku 应用。
> 更多信息：<https://www.heroku.com/>.

- 登录到你的 heroku 帐户：

`heroku login`

- 创建一个 heroku 应用：

`heroku create`

- 显示应用的日志：

`heroku logs --app {{app_name}}`

- 在 dyno（Heroku 虚拟机）中运行一次性进程：

`heroku run {{process_name}} --app {{app_name}}`

- 列出应用的 dyno（Heroku 虚拟机）：

`heroku ps --app {{app_name}}`

- 永久销毁应用：

`heroku destroy --app {{app_name}}`
