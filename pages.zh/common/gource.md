# gource

> 渲染 Git、SVN、Mercurial 和 Bazaar 仓库的动画树状图。
> 显示文件和目录随时间被创建、修改或删除的情况。
> 更多信息：<https://gource.io>。

- 在一个目录中运行 gource（如果它不是仓库的根目录，gource 会从当前目录向上查找根目录）：

`gource {{path/to/repository}}`

- 在当前目录中运行 gource，并指定自定义输出分辨率：

`gource -{{width}}x{{height}}`

- 指定动画的时间比例尺：

`gource -c {{time_scale_multiplier}}`

- 指定动画中每一天的持续时间（如果提供了 -c 选项，此选项将与之结合使用）：

`gource -s {{seconds}}`

- 使用全屏模式和自定义背景颜色：

`gource -f -b {{hex_color_code}}`

- 指定动画的标题：

`gource --title {{title}}`
