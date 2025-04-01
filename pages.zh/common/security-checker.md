# security-checker

> 检查 PHP 应用程序是否使用了已知安全漏洞的依赖项。
> 更多信息：<https://github.com/sensiolabs/security-checker>.

- 检查项目依赖中的安全问题（基于当前目录下的 `composer.lock` 文件）：

`security-checker security:check`

- 使用特定的 `composer.lock` 文件：

`security-checker security:check {{path/to/composer.lock}}`

- 以 JSON 对象的形式返回结果：

`security-checker security:check --format=json`
