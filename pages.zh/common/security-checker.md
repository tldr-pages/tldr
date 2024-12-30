# 安全检查器

> 检查 PHP 应用程序是否使用具有已知安全漏洞的依赖项。
> 更多信息：<https://github.com/sensiolabs/security-checker>。

- 在项目依赖项中查找安全问题（基于当前目录中的 `composer.lock` 文件）：

`security-checker security:check`

- 使用特定的 `composer.lock` 文件：

`security-checker security:check {{path/to/composer.lock}}`

- 以 JSON 对象的形式返回结果：

`security-checker security:check --format=json`