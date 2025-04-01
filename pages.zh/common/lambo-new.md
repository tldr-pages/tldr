# lambo new

> 一个增强版的 `laravel new`，适用于 Laravel 和 Valet。
> 更多信息：<https://github.com/tighten/lambo>.

- 创建一个新的 Laravel 应用程序：

`lambo new {{app_name}}`

- 在指定路径安装应用程序：

`lambo new --path={{path/to/directory}} {{app_name}}`

- 包含身份验证 scaffolding：

`lambo new --auth {{app_name}}`

- 包含特定的前端：

`lambo new --{{vue|bootstrap|react}} {{app_name}}`

- 项目创建后安装 `npm` 依赖：

`lambo new --node {{app_name}}`

- 项目创建后创建一个 Valet 站点：

`lambo new --link {{app_name}}`

- 创建一个与项目同名的新 MySQL 数据库：

`lambo new --create-db --dbuser={{user}} --dbpassword={{password}} {{app_name}}`

- 项目创建后打开特定的编辑器：

`lambo new --editor="{{editor}}" {{app_name}}`