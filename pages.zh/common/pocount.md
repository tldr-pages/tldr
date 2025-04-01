# pocount

> Translate Toolkit 工具，用于从文件中获取翻译进度，支持多种格式。
> 更多信息：<https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- 打印一个文件的翻译进度的彩色表格：

`pocount {{path/to/file/file.po}}`

- 打印多个文件的翻译进度，每个文件一行：

`pocount --short {{translation_*.ts}}`

- 生成一个包含多个文件翻译进度的 CSV 文件：

`pocount --csv {{translation_*.ts}} > {{path/to/translation_progress.csv}}`