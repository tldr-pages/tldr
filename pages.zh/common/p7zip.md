# p7zip

> 7-Zip 文件归档工具的包装器，具有高压缩比。
> 内部执行 7za 或 7zr 命令。
> 更多信息：<https://p7zip.sourceforge.net>。

- 压缩文件，用 7zipped 压缩版本替换原文件：

`p7zip {{path/to/file}}`

- 压缩文件，并保留输入文件：

`p7zip -k {{path/to/file}}`

- 解压文件，用原始未压缩版本替换：

`p7zip -d {{compressed.ext}}.7z`

- 解压文件，保留输入文件：

`p7zip -d -k {{compressed.ext}}.7z`

- 跳过某些检查并强制压缩或解压：

`p7zip -f {{path/to/file}}`