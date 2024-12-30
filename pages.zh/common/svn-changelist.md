# svn 变更列表

> 将变更列表与一组文件关联。
> 更多信息请访问：<https://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>。

- 将文件添加到变更列表，如果变更列表不存在则创建它：

`svn changelist {{变更列表名称}} {{路径/到/文件1}} {{路径/到/文件2}}`

- 从变更列表中移除文件：

`svn changelist --remove {{路径/到/文件1}} {{路径/到/文件2}}`

- 一次性移除整个变更列表：

`svn changelist --remove --recursive --changelist {{变更列表名称}} .`

- 将空格分隔的目录列表的内容添加到变更列表：

`svn changelist --recursive {{变更列表名称}} {{路径/到/目录1 路径/到/目录2 ...}}`

- 提交变更列表：

`svn commit --changelist {{变更列表名称}}`