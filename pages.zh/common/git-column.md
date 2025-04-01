# git column

> 以列形式显示数据。
> 更多信息：<https://git-scm.com/docs/git-column>。

- 将 `stdin` 格式化为多列：

`ls | git column --mode={{column}}`

- 将 `stdin` 格式化为多列，并设置最大宽度为 `100`：

`ls | git column --mode=column --width={{100}}`

- 将 `stdin` 格式化为多列，并设置最大填充为 `30`：

`ls | git column --mode=column --padding={{30}}`
