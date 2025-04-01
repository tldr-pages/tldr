# htmlq

> 使用 CSS 选择器从 HTML 文件中提取内容。
> 更多信息：<https://github.com/mgdm/htmlq>。

- 返回所有类为 `card` 的元素：

`cat {{path/to/file.html}} | htmlq '.card'`

- 获取第一个段落的文本内容：

`cat {{path/to/file.html}} | htmlq --text 'p:first-of-type'`

- 查找页面中的所有链接：

`cat {{path/to/file.html}} | htmlq --attribute href 'a'`

- 从页面中删除所有图像和 SVG：

`cat {{path/to/file.html}} | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- 美化并输出到文件：

`htmlq --pretty --filename {{path/to/input.html}} --output {{path/to/output.html}}`
