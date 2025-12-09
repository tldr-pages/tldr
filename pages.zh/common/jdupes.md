# jdupes

> 一个强大的重复文件查找器，并且是 fdupes 的一个增强分支。
> 更多信息：<https://codeberg.org/jbruchon/jdupes#usage>.

- 搜索单个目录：

`jdupes {{路径/到/目录}}`

- 搜索多个目录：

`jdupes {{目录1}} {{目录2}}`

- 递归地搜索所有目录：

`jdupes --recurse {{路径/到/目录}}`

- 递归地搜索目录，并让用户选择要保留的文件：

`jdupes --delete --recurse {{路径/到/目录}}`

- 搜索多个目录并跟随目录2下的子目录，而不是目录1：

`jdupes {{目录1}} --recurse: {{目录2}}`

- 搜索多个目录并在结果中保持目录顺序：

`jdupes -O {{目录1}} {{目录2}} {{目录3}}`
