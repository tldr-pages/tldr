# ddgr

> 从终端搜索 DuckDuckGo（HTML 版本）。
> 更多信息：<https://github.com/jarun/ddgr>。

- 以交互模式启动：

`ddgr`

- 在 DuckDuckGo 上搜索一个关键词：

`ddgr {{keyword}}`

- 将搜索结果的数量限制为 `N`：

`ddgr -n {{N}} {{keyword}}`

- 在搜索结果中显示完整的 URL：

`ddgr -x {{keyword}}`

- 在 DuckDuckGo 上搜索一个关键词并在浏览器中打开第一个结果：

`ddgr !w {{keyword}}`

- 执行特定网站的搜索：

`ddgr -w {{site}} {{keyword}}`

- 搜索特定文件类型：

`ddgr {{keyword}} filetype:{{filetype}}`

- 在交互模式下显示帮助：

`?`