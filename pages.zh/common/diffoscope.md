# diffoscope

> 比较文件、归档文件和目录。
> 更多信息：<https://diffoscope.org>。

- 比较两个文件：

`diffoscope {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件时不显示进度条：

`diffoscope --no-progress {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件并将 HTML 报告写入文件（使用 `-` 表示标准输出）：

`diffoscope --html {{path/to/outfile|-}} {{path/to/file1}} {{path/to/file2}}`

- 比较两个目录，排除名称匹配指定模式的文件：

`diffoscope --exclude {{pattern}} {{path/to/directory1}} {{path/to/directory2}}`

- 比较两个目录并控制是否考虑目录元数据：

`diffoscope --exclude-directory-metadata {{auto|yes|no|recursive}} {{path/to/directory1}} {{path/to/directory2}}`
