# fakedata

> 使用多种生成器生成虚拟数据。
> 更多信息：<https://github.com/lucapette/fakedata>.

- 列出所有有效的生成器：

`fakedata --generators`

- 使用一个或多个生成器生成数据：

`fakedata {{generator1}} {{generator2}}`

- 以特定的输出格式生成数据：

`fakedata --format {{csv|tab|sql}} {{generator}}`

- 生成指定数量的数据项（默认为10）：

`fakedata --limit {{n}} {{generator}}`

- 使用自定义输出模板生成数据（生成器名称的首字母必须大写）：

`echo "{{\{\{Generator\}\}}}" | fakedata`