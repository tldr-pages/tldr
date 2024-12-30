# pkgutil

> 查询和操作 Mac OS X 安装包和收据。
> 更多信息：<https://keith.github.io/xcode-man-pages/pkgutil.1.html>。

- 列出所有已安装包的包 ID：

`pkgutil --pkgs`

- 验证包文件的加密签名：

`pkgutil --check-signature {{path/to/filename.pkg}}`

- 列出给定包 ID 的已安装包的所有文件：

`pkgutil --files {{com.microsoft.Word}}`

- 将包文件的内容提取到一个目录中：

`pkgutil --expand-full {{path/to/filename.pkg}} {{path/to/directory}}`