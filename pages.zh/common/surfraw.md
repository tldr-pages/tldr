# surfraw

> 查询多种网络搜索引擎。
> 由一系列 elvi 组成，每个 elvi 知道如何搜索一个网站。
> 更多信息请访问：<http://surfraw.org>。

- 显示支持的网站搜索脚本 (elvi) 列表：

`surfraw -elvi`

- 在浏览器中打开特定搜索的 elvi 结果页面：

`surfraw {{elvi}} "{{search_terms}}"`

- 显示 elvi 描述及其特定选项：

`surfraw {{elvi}} -local-help`

- 使用具有特定选项的 elvi 进行搜索，并在浏览器中打开结果页面：

`surfraw {{elvi}} {{elvi_options}} "{{search_terms}}"`

- 显示特定搜索的 elvi 结果页面的 URL：

`surfraw -print {{elvi}} "{{search_terms}}"`

- 使用别名进行搜索：

`sr {{elvi}} "{{search_terms}}"`