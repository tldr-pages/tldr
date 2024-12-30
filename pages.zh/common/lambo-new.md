# lambo 新版

> 一个为 Laravel 和 Valet 提供超级强大功能的 `laravel new`。
> 更多信息请访问：<https://github.com/tighten/lambo>。

- 创建一个新的 Laravel 应用：

`lambo new {{app_name}}`

- 在特定路径安装应用：

`lambo new --path={{path/to/directory}} {{app_name}}`

- 包含认证脚手架：

`lambo new --auth {{app_name}}`

- 包含特定前端：

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- 在项目创建后安装 `npm` 依赖：

`lambo new --node {{app_name}}`

- 在项目创建后创建一个 Valet 站点：

`lambo new --link {{app_name}}`

- 创建一个与项目同名的新 MySQL 数据库：

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- 在项目创建后打开特定编辑器：

`lambo new --editor="{{editor}}" {{app_name}}`