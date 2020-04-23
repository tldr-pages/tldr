# vim

> Vi IMproved, 一个程序员的文本编辑器，提供为不同类型的文档修改设计的多种模式
> 在`vim`内使用任何命令时请确认未使用中文输入法，否则可能会出现奇怪的问题
> 按下`i`来进入编辑模式，`<esc>`回到标准模式 （不允许普通的字符输入）
> 更多信息：<https://www.vim.org>.

- 打开文档:

`vim {{file}}`

- 进入编辑模式 （插入模式）:

`<Esc>i`

- 复制 ("yank") 或剪切 ("delete") 当前行 （使用`P`来粘贴）:

`<Esc>{{yy|dd}}`

- 撤销上一个操作:

`<Esc>u`

- 在文件中搜寻 （按下 `n`/`N` 来在上一个 / 下一个结果中切换）:

`<Esc>/{{search_pattern}}<Enter>`

- 对整个文件使用正则表达式进行替换:

`<Esc>:%s/{{pattern}}/{{replacement}}/g<Enter>`

- 保存 （写入） 文件，然后退出:

`<Esc>:wq<Enter>`

- 不保存退出:

`<Esc>:q!<Enter>`
