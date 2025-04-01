# svn changelist

> 将更改列表与一组文件关联。
> 更多信息：<https://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>。

- 将文件添加到更改列表，如果更改列表不存在则创建它：

`svn changelist {{changelist_name}} {{path/to/file1}} {{path/to/file2}}`

- 从更改列表中移除文件：

`svn changelist --remove {{path/to/file1}} {{path/to/file2}}`

- 一次性移除整个更改列表：

`svn changelist --remove --recursive --changelist {{changelist_name}} .`

- 将空格分隔的目录列表中的内容添加到更改列表：

`svn changelist --recursive {{changelist_name}} {{path/to/directory1 path/to/directory2 ...}}`

- 提交更改列表：

`svn commit --changelist {{changelist_name}}`