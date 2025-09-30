# more

> `stdin` またはファイルからのページ分割された出力を表示します。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>。

- `stdin`の出力をページ分割して表示する:

`{{echo test}} | more`

- 1つ以上のファイルからページ分割された出力を表示する:

`more {{path\to\file}}`

- タブを指定した数のスペースに変換する:

`more {{path\to\file}} /t{{スペース数}}`

- ページを表示する前に画面をクリアする:

`more {{path\to\file}} /c`

- 5行目からの出力を表示する:

`more {{path\to\file}} +{{5}}`

- 拡張インタラクティブモードを有効にする(使い方はヘルプを参照):

`more {{path\to\file}} /e`

- ヘルプを表示する:

`more /?`
