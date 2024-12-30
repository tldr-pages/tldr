# Composer

> 一个基于包的 PHP 项目依赖管理工具。
> 更多信息请访问：<https://getcomposer.org/>。

- 交互式创建 `composer.json` 文件：

`composer init`

- 将一个包添加为该项目的依赖，并在 `composer.json` 中添加条目：

`composer require {{user/package}}`

- 安装该项目 `composer.json` 中的所有依赖，并创建 `composer.lock` 文件：

`composer install`

- 从该项目中卸载一个包，移除其在 `composer.json` 和 `composer.lock` 中的依赖：

`composer remove {{user/package}}`

- 更新该项目 `composer.json` 中的所有依赖，并在 `composer.lock` 文件中记录新版本：

`composer update`

- 在手动更新 `composer.json` 后，仅更新 `composer.lock`：

`composer update --lock`

- 了解为什么无法安装某个依赖：

`composer why-not {{user/package}}`

- 将 Composer 更新到最新版本：

`composer self-update`