# git column

> 以列格式显示数据。
> 更多信息：<https://git-scm.com/docs/git-column>.

- 将标准输入内容格式化为多列显示：

`ls | git column --mode={{column}}`

- 以最大宽度 `100` 的列格式显示标准输入内容：

`ls | git column --mode=column --width={{100}}`

- 以最大边距 `30` 的列格式显示标准输入内容：

`ls | git column --mode=column --padding={{30}}`
