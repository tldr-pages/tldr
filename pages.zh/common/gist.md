# gist

> 将代码上传到 <https://gist.github.com>。
> 更多信息：<https://github.com/defunkt/gist>。

- 在这台电脑上登录 gist：

`gist --login`

- 从任意数量的文本文件创建一个 gist：

`gist {{file.txt}} {{file2.txt}}`

- 创建一个带有描述的私有 gist：

`gist --private --description "{{一个有意义的描述}}" {{file.txt}}`

- 从 `stdin` 读取内容并创建一个 gist：

`{{echo "hello world"}} | gist`

- 列出你的公共和私有 gists：

`gist --list`

- 列出任何用户的所有公共 gists：

`gist --list {{username}}`

- 使用 URL 中的 ID 更新一个 gist：

`gist --update {{GIST_ID}} {{file.txt}}`