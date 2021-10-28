# zip

> 将文件打包并压缩（存档）为 zip 文件。
> 更多信息： <https://manned.org/zip>.

- 递归地打包和压缩文件和目录：

`zip -r {{compressed.zip}} {{path/to/file}} {{path/to/directory1}} {{path/to/directory2}}`

- 添加到压缩档案中并排除不需要的文件：

`zip -r {{compressed.zip}} {{path/to/directory}} -x {{path/to/exclude}}`

- 使用最高压缩级别 9 归档目录及其内容：

`zip -r -{{9}} {{compressed.zip}} {{path/to/directory}}`

- 创建一个加密档案（用户将被提示输入密码）：

`zip -e -r {{compressed.zip}} {{path/to/directory}}`

- 将文件添加到现有的 zip 文件：

`zip {{compressed.zip}} {{path/to/file}}`

- 从现有 zip 文件中删除文件：

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`

- 将目录及其内容存档到多个拆分的 zip 文件（例如：每个 3 GB 的包）：

`zip -r -s {{3g}} {{compressed.zip}} {{path/to/directory}}`

- 列出指定存档中的文件（不提取文件）：

`zip -sf {{compressed.zip}}`
