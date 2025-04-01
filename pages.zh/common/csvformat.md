# csvformat

> 将 CSV 文件转换为自定义输出格式。
> 包含在 csvkit 中。
> 更多信息：<https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- 转换为制表符分隔的文件（TSV）：

`csvformat -T {{data.csv}}`

- 将分隔符转换为自定义字符：

`csvformat -D "{{custom_character}}" {{data.csv}}`

- 将换行符转换为回车（^M）+ 换行：

`csvformat -M "{{\r\n}}" {{data.csv}}`

- 尽量减少使用引号字符：

`csvformat -U 0 {{data.csv}}`

- 尽量多使用引号字符：

`csvformat -U 1 {{data.csv}}`