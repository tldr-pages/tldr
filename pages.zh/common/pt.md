# pt

> 铂金搜索器。
> 一种类似于 `ag` 的代码搜索工具。
> 更多信息：<https://github.com/monochromegane/the_platinum_searcher>。

- 查找包含 "foo" 的文件并打印带有高亮匹配的文件：

`pt {{foo}}`

- 查找包含 "foo" 的文件并显示每个文件中匹配的数量：

`pt -c {{foo}}`

- 查找包含 "foo" 的整个单词并忽略其大小写：

`pt -wi {{foo}}`

- 使用正则表达式在具有特定扩展名的文件中查找 "foo"：

`pt -G='{{\.bar$}}' {{foo}}`

- 查找其内容匹配正则表达式的文件，最多深入 2 个目录：

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`