# surfraw

> 查询各种网络搜索引擎。
> 包含一系列的 elvi，每个 elvi 都知道如何搜索特定的网站。
> 更多信息：<http://surfraw.org>。

- 显示支持的网站搜索脚本（elvi）列表：

`surfraw -elvi`

- 在浏览器中打开特定搜索的 elvi 结果页面：

`surfraw {{elvi}} "{{search_terms}}"`

- 显示 elvi 的描述及其特定选项：

`surfraw {{elvi}} -local-help`

- 使用特定选项的 elvi 进行搜索并在浏览器中打开结果页面：

`surfraw {{elvi}} {{elvi_options}} "{{search_terms}}"`

- 显示特定搜索的 elvi 结果页面的 URL：

`surfraw -print {{elvi}} "{{search_terms}}"`

- 使用别名进行搜索：

`sr {{elvi}} "{{search_terms}}"`
