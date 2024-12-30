# gource

> 渲染 Git、SVN、Mercurial 和 Bazaar 仓库的动画树状图。
> 它展示了文件和目录随时间的创建、修改或删除。
> 更多信息：<https://gource.io>。

- 在一个目录中运行 gource（如果不是仓库的根目录，将从该目录向上查找根目录）：

`gource {{path/to/repository}}`

- 在当前目录中运行 gource，并指定自定义输出分辨率：

`gource -{{width}}x{{height}}`

- 指定动画的时间尺度：

`gource -c {{time_scale_multiplier}}`

- 指定动画中每一天的时长（如果提供了 -c，该选项将与之结合）：

`gource -s {{seconds}}`

- 使用全屏模式和自定义背景颜色：

`gource -f -b {{hex_color_code}}`

- 指定动画标题：

`gource --title {{title}}`