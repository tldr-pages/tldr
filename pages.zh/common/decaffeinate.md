# 去咖啡因

> 将你的 CoffeeScript 源代码转换为现代 JavaScript。
> 更多信息：<https://decaffeinate-project.org>。

- 将 CoffeeScript 文件转换为 JavaScript：

`decaffeinate {{path/to/file.coffee}}`

- 将 CoffeeScript v2 文件转换为 JavaScript：

`decaffeinate --use-cs2 {{path/to/file.coffee}}`

- 将 require 和 `module.exports` 转换为 import 和 export：

`decaffeinate --use-js-modules {{path/to/file.coffee}}`

- 将 CoffeeScript 转换，允许命名导出：

`decaffeinate --loose-js-modules {{path/to/file.coffee}}`