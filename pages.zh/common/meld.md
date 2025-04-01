# meld

> 图形化的差异比较和合并工具。
> 更多信息：<https://meldmerge.org/>.

- 启动 `meld`:

`meld`

- 比较两个文件:

`meld {{path/to/file_1}} {{path/to/file_2}}`

- 比较两个目录:

`meld {{path/to/directory_1}} {{path/to/directory_2}}`

- 比较三个文件:

`meld {{path/to/file_1}} {{path/to/file_2}} {{path/to/file_3}}`

- 在已存在的 meld 实例中以新标签页打开比较:

`meld --newtab {{path/to/file_1}} {{path/to/file_2}}`

- 比较多组文件:

`meld --diff {{path/to/file_1}} {{path/to/file_2}} --diff {{path/to/file_3}} {{path/to/file_4}}`
