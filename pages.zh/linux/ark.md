# ark

> KDE的归档工具。
> 更多信息：<https://docs.kde.org/stable5/zh/ark/ark/>.

- 将特定归档提取到当前目录：

`ark --batch {{path/to/archive}}`

- 将归档提取到特定目录：

`ark --batch --destination {{path/to/directory}} {{path/to/archive}}`

- 如果归档不存在，则创建一个并将特定文件添加到其中：

`ark --add-to {{path/to/archive}} {{path/to/file1 path/to/file2 ...}}`