# polybar

> 一个快速且易于使用的状态栏。
> 更多信息：<https://github.com/polybar/polybar/wiki>。

- 启动 Polybar（如果在配置中只定义了一个栏，则栏名是可选的）：

`polybar {{bar_name}}`

- 使用指定的配置启动 Polybar：

`polybar --config={{path/to/config.ini}} {{bar_name}}`

- 启动 Polybar，并在配置文件修改时重新加载栏：

`polybar --reload {{bar_name}}`