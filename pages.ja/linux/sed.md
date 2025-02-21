# sed

> スクリプタブルな方法でテキストを編集します。
> `awk`, `ed` も参照してください。
> もっと詳しく: <https://www.gnu.org/software/sed/manual/sed.html>。

- 全ての入力行の `apple` (基本正規表現)を `mango` (基本正規表現)に置換し、結果を`stdout`に出力する:

`{{command}} | sed 's/apple/mango/g'`

- 全ての入力行で出現する全ての `apple` (拡張正規表現)を `APPLE` (拡張正規表現)に置換し、結果を`stdout`に出力する:

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- 特定のファイルに出現する全ての `apple` (基本正規表現)を `mango` (基本正規表現)に置換し、元のファイルを上書きする:

`sed -i 's/apple/mango/g' {{path/to/file}}`

- 特定のスクリプトファイル([f]ile)を実行し、結果を`stdout`に出力する:

`{{command}} | sed -f {{path/to/script.sed}}`

- 最初の行だけを`stdout`に出力する:

`{{command}} | sed -n '1p'`

- ファイルの最初の行を削除([d]elete)する:

`sed -i 1d {{path/to/file}}`

- ファイルの先頭行に改行を挿入([i]nsert)する:

`sed -i '1i\your new line text\' {{path/to/file}}`
