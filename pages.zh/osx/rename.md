# 重命名

> 使用正则表达式重命名文件或文件组。
> 更多信息：<https://keith.github.io/xcode-man-pages/rename.2.html>。

- 在指定文件的文件名中将 `from` 替换为 `to`：

`rename 's/{{from}}/{{to}}/' {{*.txt}}`