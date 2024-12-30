# zgrep

> 从压缩文件中提取文本模式（等同于 `grep -Z`）。
> 更多信息：<https://manned.org/zgrep>。

- 在压缩文件中查找模式（区分大小写）：

`zgrep {{pattern}} {{path/to/compressed/file}}`

- 在压缩文件中查找模式（不区分大小写）：

`zgrep -i {{pattern}} {{path/to/compressed/file}}`

- 输出压缩文件中包含匹配模式的行数：

`zgrep -c {{pattern}} {{path/to/compressed/file}}`

- 显示不包含该模式的行（反向搜索功能）：

`zgrep -v {{pattern}} {{path/to/compressed/file}}`

- 在压缩文件中查找多个模式：

`zgrep -e "{{pattern_1}}" -e "{{pattern_2}}" {{path/to/compressed/file}}`

- 使用扩展正则表达式（支持 `?`、`+`、`{}`、`()` 和 `|`）：

`zgrep -E {{regular_expression}} {{path/to/file}}`

- 打印每个匹配项周围的 3 行 [C]ontext、[B]efore 或 [A]fter：

`zgrep -{{C|B|A}} {{3}} {{pattern}} {{path/to/compressed/file}}`