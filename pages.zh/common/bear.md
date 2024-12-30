# bear

> 一个用于生成 `clang` 工具编译数据库的工具。
> 更多信息请访问：<https://github.com/rizsotto/Bear>。

- 通过运行构建命令生成 `compile_commands.json`：

`bear -- {{make}}`

- 使用自定义输出文件名生成编译数据库：

`bear --output {{path/to/compile_commands.json}} -- {{make}}`

- 将结果附加到现有的 `compile_commands.json` 文件：

`bear --append -- {{make}}`

- 以详细模式运行以获取详细输出：

`bear --verbose -- {{make}}`

- 强制 `bear` 使用预加载方法进行命令拦截：

`bear --force-preload -- {{make}}`