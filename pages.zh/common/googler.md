# googler

> 从命令行搜索 Google。
> 更多信息：<https://github.com/jarun/googler>.

- 搜索 Google 指定的关键词：

`googler {{keyword}}`

- 搜索 Google 并在网页浏览器中打开第一个结果：

`googler -j {{keyword}}`

- 显示 `n` 个搜索结果（默认：10 个）：

`googler -n {{n}} {{keyword}}`

- 禁用自动拼写纠正：

`googler -x {{keyword}}`

- 在指定网站上搜索关键词：

`googler -w {{site}} {{keyword}}`

- 以 JSON 格式显示 Google 搜索结果：

`googler --json {{keyword}}`

- 进行原地自升级：

`googler -u`

- 在交互模式下显示帮助：

`<?>`
