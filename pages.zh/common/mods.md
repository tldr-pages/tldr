# mods

> 为命令行构建的 AI，旨在用于管道。
> 更多信息：<https://github.com/charmbracelet/mods>。

- 提出一个通用问题：

`mods "{{给我写一首关于鸭嘴兽的诗}}"`

- 在你的 `$EDITOR` 中打开设置：

`mods --settings`

- 请求对你的代码进行评论，采用 markdown 格式：

`mods --format "{{你对改进这段代码有什么想法？}}" < {{path/to/file}}`

- 请求帮助你的文档，采用 markdown 格式：

`mods --format "{{为这个 README 写一个新部分，介绍一个功能：如果你按下 r，会给你发送一只免费的兔子}}" < {{README.md}}`

- 以 markdown 格式组织你的视频：

`ls {{path/to/videos}} | mods --format "{{按年代组织这些视频并进行总结}}"`

- 通读原始 HTML 并总结内容，采用 markdown 格式：

`curl "{{https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m}}" | mods --format "{{为人类总结这些天气数据}}"`

- 显示帮助信息：

`mods --help`