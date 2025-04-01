# git sed

> 使用 sed 替换 git 管理的文件中的模式。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>。

- 替换当前仓库中指定的文本：

`git sed '{{find_text}}' '{{replace_text}}'`

- 替换指定的文本，并使用标准提交信息提交更改：

`git sed -c '{{find_text}}' '{{replace_text}}'`

- 使用正则表达式替换指定的文本：

`git sed -f g '{{find_text}}' '{{replace_text}}'`

- 替换指定目录下所有文件中的特定文本：

`git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}`
