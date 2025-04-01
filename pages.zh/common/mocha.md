# mocha

> 一个功能丰富的 JavaScript 测试框架。
> 更多信息：<https://mochajs.org>。

- 使用默认配置或 `mocha.opts` 中配置的设置运行测试：

`mocha`

- 运行位于特定位置的测试：

`mocha {{directory/with/tests}}`

- 运行与特定 `grep` 模式匹配的测试：

`mocha --grep {{regular_expression}}`

- 在当前目录中的 JavaScript 文件发生更改时运行测试，并且初次运行一次：

`mocha --watch`

- 使用特定的报告器运行测试：

`mocha --reporter {{reporter}}`