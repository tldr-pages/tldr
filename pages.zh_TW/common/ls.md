# ls

> 列出目錄內容。
> 更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- 列出目錄中的檔案，其中每個檔案佔一行：

`ls -1`

- 列出包含隱藏檔案的所有檔案：

`ls {{[-a|--all]}}`

- 列出檔案，並依照檔案類型在檔案後面加上對應的符號（例如目錄會加上「/」）：

`ls {{[-F|--classify]}}`

- 列出包含隱藏檔案的完整檔案列表（包括權限、擁有者、檔案大小與修改日期）：

`ls {{[-la|--all -l]}}`

- 列出完整檔案列表，其中檔案大小會用 KiB、MiB、GiB 表示：

`ls {{[-lh|-l --human-readable]}}`

- 列出完整檔案列表，並依檔案大小降序排序：

`ls {{-lSR|-lS --recursive}}`

- 列出完整檔案列表，並依修改時間由舊到新排序：

`ls {{[-ltr|-lt --reverse]}}`
