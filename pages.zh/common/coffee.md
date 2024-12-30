# 咖啡

> 执行 CoffeeScript 脚本或将其编译为 JavaScript。
> 更多信息：<https://coffeescript.org#cli>。

- 运行脚本：

`coffee {{path/to/file.coffee}}`

- 编译为 JavaScript 并保存为同名文件：

`coffee --compile {{path/to/file.coffee}}`

- 编译为 JavaScript 并保存为指定的输出文件：

`coffee --compile {{path/to/file.coffee}} --output {{path/to/file.js}}`

- 启动 REPL（交互式 Shell）：

`coffee --interactive`

- 监视脚本的变化并重新运行脚本：

`coffee --watch {{path/to/file.coffee}}`