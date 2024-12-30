# phpenv

> 一款用于开发目的的 PHP 版本管理器。
> 更多信息请访问: <https://github.com/phpenv/phpenv>。

- 全局安装一个 PHP 版本：

`phpenv install {{version}}`

- 刷新所有已知的 `phpenv` PHP 二进制文件的 shim 文件：

`phpenv rehash`

- 列出所有已安装的 PHP 版本：

`phpenv versions`

- 显示当前活动的 PHP 版本：

`phpenv version`

- 设置全局 PHP 版本：

`phpenv global {{version}}`

- 设置本地 PHP 版本，它会覆盖全局版本：

`phpenv local {{version}}`

- 取消设置本地 PHP 版本：

`phpenv local --unset`