# mocha

> 一款功能丰富的 JavaScript 测试框架。
> 更多信息请访问: <https://mochajs.org>。

- 使用默认配置或在 `mocha.opts` 中配置的方式运行测试：

`mocha`

- 运行特定位置的测试：

`mocha {{目录/包含测试}}`

- 运行匹配特定 `grep` 模式的测试：

`mocha --grep {{正则表达式}}`

- 在当前目录的 JavaScript 文件发生更改时运行测试，并首次运行：

`mocha --watch`

- 使用特定的报告器运行测试：

`mocha --reporter {{报告器}}`