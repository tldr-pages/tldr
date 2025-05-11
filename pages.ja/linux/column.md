# column

> `stdin` またはファイルを複数の列にフォーマットします。
> デフォルトの区切り文字は空白文字です。
> もっと詳しく: <https://manned.org/column>。

- 30文字幅の表示用にコマンドの出力をフォーマットする:

`printf "header1 header2\nbar foo\n" | column {{[-c|--output-width]}} {{30}}`

- カラムを自動的に分割し、表形式に自動整列する:

`printf "header1 header2\nbar foo\n" | column {{[-t|--table]}}`

- `table`オプションにカラムの区切り文字を指定する(CSVの場合は","など) (デフォルトは空白文字):

`printf "header1,header2\nbar,foo\n" | column {{[-t|--table]}} {{[-s|--separator]}} {{,}}`

- 列を埋める前に行を埋める:

`printf "header1\nbar\nfoobar\n" | column {{[-c|--output-width]}} {{30}} {{[-x|--fillrows]}}`
