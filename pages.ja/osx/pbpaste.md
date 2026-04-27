# pbpaste

> クリップボードの内容を`stdout`(標準出力)に送信します。
> これは、キーボードの`<Cmd v>`を押す操作に相当します。
> 詳細情報: <https://keith.github.io/xcode-man-pages/pbcopy.1>。

- クリップボードの内容をファイルに書き出す:

`pbpaste > {{パス/宛先/ファイル}}`

- クリップボードの内容をコマンドの入力として使用する:

`pbpaste | {{grep 検索文字列}}`
