# sed

> 以脚本方式编辑文本。
> 参见：`awk`, `ed`.
> 更多信息：<https://www.gnu.org/software/sed/manual/sed.html>.

- 将所有输入行中出现的 `apple`（基本正则语法）替换为 `mango`（基本正则语法），并将结果打印到 `stdout`：

`{{命令}} | sed 's/apple/mango/g'`

- 将所有输入行中出现的 `apple`（扩展正则语法）替换为 `APPLE` （扩展正则语法），并将结果打印到 `stdout`：

`{{命令}} | sed -E 's/(apple)/\U\1/g'`

- 用 `mango`（基本正则语法）替换特定文件中出现的所有 `apple`（基本正则语法），并覆盖原文件：

`sed -i 's/apple/mango/g' {{路径/到/文件}}`

- 执行特定的脚本，并将结果打印到 `stdout`：

`{{命令}} | sed -f {{路径/到/脚本.sed}}`

- 打印第一行到 `stdout`：

`{{命令}} | sed -n '1p'`

- 删除文件第一行：

`sed -i 1d {{路径/到/文件}}`

- 插入新行到文件的第一行：

`sed -i '1i\your new line text\' {{路径/到/文件}}`
