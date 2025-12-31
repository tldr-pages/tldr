# df

> ファイルシステムのディスク使用量の概要を表示します。
> もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>。

- すべてのファイルシステムとそのディスク使用量を表示する:

`df`

- すべてのファイルシステムとそのディスク使用量を、人が解釈可能な形式で表示する:

`df {{[-h|--human-readable]}}`

- 与えられたファイルまたはディレクトリを含むファイルシステムと、そのディスク使用量を表示する:

`df {{path/to/file_or_directory}}`

- 空きinode数の統計を含める:

`df {{[-i|--inodes]}}`

- ファイルシステムを表示するが、指定したタイプは除外する:

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- ファイルシステムのタイプを表示する:

`df {{[-T|--print-type]}}`
