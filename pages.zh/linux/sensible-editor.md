# sensible-editor

> 打开默认编辑器。
> 更多信息：<https://manned.org/sensible-editor>.

- 在默认编辑器中打开文件：

`sensible-editor {{path/to/file}}`

- 在默认编辑器中打开文件，并将光标置于文件末尾：

`sensible-editor + {{path/to/file}}`

- 在默认编辑器中打开文件，并将光标置于第10行的开头：

`sensible-editor +10 {{path/to/file}}`

- 同时在垂直分割的编辑器窗口中打开3个文件：

`sensible-editor -O3 {{path/to/file1 path/to/file2 path/to/file3}}`