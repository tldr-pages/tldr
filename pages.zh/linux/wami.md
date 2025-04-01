# wami

> 一个开源且易于使用的工具，可以为任务推荐合适的程序。
> 更多信息：<https://github.com/evait-security/wami>.

- 在所有类别中查找扩展结果，并按指定顺序排序：

`wami --show-all -S {{asc|desc}} --search-all {{search_string}}`

- 在 GitHub 中查找扩展结果，并按降序排序：

`wami --show-all -S desc --github {{search_string}}`

- 在 GitHub 中查找与搜索字符串匹配的主题：

`wami --list-topics {{search_string}}`

- 在 lake 中查找用于渗透测试以查询默认凭据的工具，并按降序排序结果：

`wami -S desc --search-all pentest credential default`