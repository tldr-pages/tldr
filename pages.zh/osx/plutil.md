# plutil

> 查看、转换、验证或编辑属性列表（"plist"）文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/plutil.1.html>.

- 以可读格式显示一个或多个 plist 文件的内容：

`plutil -p {{file1.plist file2.plist ...}}`

- 将一个或多个 plist 文件转换为 XML 格式，并覆盖原始文件：

`plutil -convert xml1 {{file1.plist file2.plist ...}}`

- 将一个或多个 plist 文件转换为二进制格式，并覆盖原始文件：

`plutil -convert binary1 {{file1.plist file2.plist ...}}`

- 将一个 plist 文件转换为其他格式，并写入新文件：

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o {{path/to/new_file.plist}}`

- 将一个 plist 文件转换为其他格式，并写入 `stdout`：

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o -`