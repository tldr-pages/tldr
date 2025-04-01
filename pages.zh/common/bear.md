# bear

> 一个用于为 `clang` 工具生成编译数据库的工具。
> 更多信息：<https://github.com/rizsotto/Bear>.

- 通过运行构建命令生成 `compile_commands.json`：

`bear -- {{make}}`

- 使用自定义输出文件名生成编译数据库：

`bear --output {{path/to/compile_commands.json}} -- {{make}}`

- 将结果追加到现有的 `compile_commands.json` 文件中：

`bear --append -- {{make}}`

- 以详细模式运行以获取详细输出：

`bear --verbose -- {{make}}`

- 强制 `bear` 使用预加载方法进行命令拦截：

`bear --force-preload -- {{make}}`