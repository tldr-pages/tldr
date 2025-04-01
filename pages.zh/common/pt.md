# pt

> Platinum Searcher。
> 一个类似于 `ag` 的代码搜索工具。
> 更多信息：<https://github.com/monochromegane/the_platinum_searcher>。

- 查找包含 "foo" 的文件并打印带有高亮匹配的文件：

`pt {{foo}}`

- 查找包含 "foo" 的文件并显示每个文件中的匹配次数：

`pt -c {{foo}}`

- 查找包含 "foo" 的整个单词并忽略大小写：

`pt -wi {{foo}}`

- 使用正则表达式在具有指定扩展名的文件中查找 "foo"：

`pt -G='{{\.bar$}}' {{foo}}`

- 查找内容与正则表达式匹配的文件，深度不超过2级目录：

`pt --depth={{2}} -e '{{^ba[rz]*$}}'`