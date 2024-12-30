# fossil 提交

> 将文件提交到 Fossil 仓库。
> 更多信息：<https://fossil-scm.org/home/help/commit>。

- 创建一个新版本，包含当前检出的所有更改；系统会提示用户输入评论：

`fossil commit`

- 创建一个新版本，包含当前检出的所有更改，使用指定的评论：

`fossil commit --comment "{{comment}}"`

- 创建一个新版本，包含当前检出的所有更改，评论从指定文件中读取：

`fossil commit --message-file {{path/to/commit_message_file}}`

- 创建一个新版本，包含来自指定文件的更改；系统会提示用户输入评论：

`fossil commit {{path/to/file1 path/to/file2 ...}}`