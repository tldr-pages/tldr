# bat

> 可以打印并且合并文件的命令.
> `cat`的复制品，外加无法高亮和git集成.
> 详见: <https://github.com/sharkdp/bat>.

- 文件内容打印:

`bat {{file}}`

- 多文件合并到目标文件:

`bat {{file1}} {{file2}} > {{target_file}}`

- 在指定文件后追加多个文件合并的内容:

`bat {{file1}} {{file2}} >> {{target_file}}`

- 打印时，显示行号:

`bat -n {{file}}`

- 高亮一个json文件:

`bat --language json {{file.json}}`

- 受支持的语言清单:

`bat --list-languages`
