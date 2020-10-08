# find

> 1つ以上のファイルで指定された文字列を検索します
> 詳しくはこちら: <https://docs.microsoft.com/windows-server/administration/windows-commands/find>.

- 指定された文字列を含む行を検索します:

`find {{string}} {{path/to/file_or_directory}}`

- 指定された文字列を含まない行を表示します:

`find {{string}} {{path/to/file_or_directory}} /v`

- 指定された文字列を含む行数を表示します:

`find {{string}} {{path/to/file_or_directory}} /c`

- 行リストとともに行番号を表示します:

`find {{string}} {{path/to/file_or_directory}} /n`
