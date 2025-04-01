# x_x

> 查看 Excel 和 CSV 文件。
> 更多信息：<https://github.com/kristianperkins/x_x>.

- 查看 XLSX 或 CSV 文件：

`x_x {{file.xlsx|file.csv}}`

- 查看 XLSX 或 CSV 文件，并使用第一行作为表头：

`x_x -h {{0}} {{file.xlsx|file.csv}}`

- 查看使用非标准分隔符的 CSV 文件：

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{file.csv}}`