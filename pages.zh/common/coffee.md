# coffee

> 执行 CoffeeScript 脚本或将它们编译为 JavaScript。
> 更多信息：<https://coffeescript.org#cli>.

- 运行脚本：

`coffee {{path/to/file.coffee}}`

- 编译为 JavaScript 并保存到同名文件：

`coffee --compile {{path/to/file.coffee}}`

- 编译为 JavaScript 并保存到指定的输出文件：

`coffee --compile {{path/to/file.coffee}} --output {{path/to/file.js}}`

- 启动 REPL（交互式 shell）：

`coffee --interactive`

- 监视脚本的更改并重新运行脚本：

`coffee --watch {{path/to/file.coffee}}`