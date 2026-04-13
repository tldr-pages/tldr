# pbpaste

> クリップボードの内容を標準出力に送信します。
> これは、キーボードの`<Cmd c>`を押す操作に相当します。
> Comparable to pressing `<Cmd v>` on the keyboard.
> 詳細情報: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>。

- クリップボードの内容をファイルに書き出す:

`pbpaste > {{ファイルへのパス}}`

- クリップボードの内容をコマンドの入力として使用する:

`pbpaste | {{grep 検索文字列}}`
