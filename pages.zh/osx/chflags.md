# chflags

> 更改文件或目录标志。
> 更多信息：<https://keith.github.io/xcode-man-pages/chflags.1.html>。

- 为文件设置 `hidden` 标志：

`chflags {{hidden}} {{path/to/file}}`

- 为文件取消设置 `hidden` 标志：

`chflags {{nohidden}} {{path/to/file}}`

- 递归地为目录设置 `uchg` 标志：

`chflags -R {{uchg}} {{path/to/directory}}`

- 递归地为目录取消设置 `uchg` 标志：

`chflags -R {{nouchg}} {{path/to/directory}}`