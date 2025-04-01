# composer

> PHP 项目的基于包的依赖管理工具。
> 更多信息：<https://getcomposer.org/>。

- 交互式创建 `composer.json` 文件：

`composer init`

- 为项目添加一个包作为依赖，并在 `composer.json` 中添加条目：

`composer require {{user/package}}`

- 安装项目 `composer.json` 中的所有依赖，并创建 `composer.lock`：

`composer install`

- 从项目中卸载一个包，从 `composer.json` 和 `composer.lock` 中移除该依赖：

`composer remove {{user/package}}`

- 更新项目 `composer.json` 中的所有依赖，并在 `composer.lock` 文件中记录新版本：

`composer update`

- 手动更新 `composer.json` 后，仅更新 `composer.lock`：

`composer update --lock`

- 了解为什么某个依赖无法安装：

`composer why-not {{user/package}}`

- 将 composer 更新到最新版本：

`composer self-update`