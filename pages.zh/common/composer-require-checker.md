# composer-require-checker

> 分析 Composer 依赖项以查找软依赖。
> 更多信息：<https://github.com/maglnet/ComposerRequireChecker>。

- 分析一个 Composer JSON 文件：

`composer-require-checker check {{path/to/composer.json}}`

- 使用特定配置分析一个 Composer JSON 文件：

`composer-require-checker check --config-file {{path/to/config.json}} {{path/to/composer.json}}`