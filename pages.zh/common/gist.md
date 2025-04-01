# gist

> 上传代码到 <https://gist.github.com>。
> 更多信息：<https://github.com/defunkt/gist>。

- 在此计算机上登录到 gist：

`gist --login`

- 从任意数量的文本文件创建 gist：

`gist {{file.txt}} {{file2.txt}}`

- 创建一个带有描述的私有 gist：

`gist --private --description "{{有意义的描述}}" {{file.txt}}`

- 从 `stdin` 读取内容并创建 gist：

`{{echo "hello world"}} | gist`

- 列出您的公共和私有 gist：

`gist --list`

- 列出任何用户的公共 gist：

`gist --list {{username}}`

- 使用 URL 中的 ID 更新 gist：

`gist --update {{GIST_ID}} {{file.txt}}`
