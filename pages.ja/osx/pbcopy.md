# pbcopy

> `stdin`(標準入力)からデータをクリップボードにコピーします。
> これは、キーボードの`<Cmd c>`を押す操作に相当します。
> 詳細情報: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>。

- 指定したファイルの内容をクリップボードにコピーします:

`pbcopy < {{パス/宛先/ファイル}}`

- 特定のコマンドの実行結果をクリップボードにコピーします:

`find . -type t -name "*.png" | pbcopy`
