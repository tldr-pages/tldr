# pbcopy

> 標準入力からデータをクリップボードにコピーします。
> これは、キーボードの`<Cmd c>`を押す操作に相当します。
> 詳細情報: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>

- 指定したファイルの内容をクリップボードにコピーします:

`pbcopy < {{path/to/file}}`

- 特定のコマンドの実行結果をクリップボードにコピーします:

`find . -type t -name "*.png" | pbcopy`
