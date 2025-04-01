# mods

> 为命令行构建的人工智能，专为管道设计。
> 更多信息：<https://github.com/charmbracelet/mods>.

- 提出一个通用问题：

`mods "{{给我写一首关于鸭嘴兽的诗}}"`

- 在你的 `$EDITOR` 中打开设置：

`mods --settings`

- 请求对你代码的评论，以 Markdown 格式：

`mods --format "{{你对改进这段代码有什么看法？}}" < {{path/to/file}}`

- 请求帮助编写文档，以 Markdown 格式：

`mods --format "{{为这个 README 添加一个新部分，描述如果用户按下 r 键，会免费收到一只兔子的功能}}" < {{README.md}}`

- 组织你的视频，以 Markdown 格式：

`ls {{path/to/videos}} | mods --format "{{按十年组织这些视频并总结}}"`

- 阅读原始 HTML 并总结内容，以 Markdown 格式：

`curl "{{https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m}}" | mods --format "{{为人类总结这些天气数据}}"`

- 显示帮助：

`mods --help`