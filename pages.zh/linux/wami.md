# wami

> 一个开源且易于使用的工具，可以推荐适合任务的程序。
> 更多信息：<https://github.com/evait-security/wami>。

- 从 lake 中找到所有类别的扩展结果并按指定顺序 [S]ort：

`wami --show-all -S {{asc|desc}} --search-all {{search_string}}`

- 在 GitHub 上搜索以查找扩展结果，并按降序 [S]orted：

`wami --show-all -S desc --github {{search_string}}`

- 在 GitHub 上搜索与搜索字符串匹配的主题：

`wami --list-topics {{search_string}}`

- 在 lake 中搜索用于渗透测试的工具，以查询默认凭据并按降序 [S]ort 结果：

`wami -S desc --search-all pentest credential default`