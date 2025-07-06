# grep

> 正規表現を使ってファイルのパターンを見つけます。
> もっと詳しく: <https://www.gnu.org/software/grep/manual/grep.html>。

- ファイル内のパターンを検索する:

`grep "{{検索パターン}}" {{path/to/file}}`

- 正確な文字列を検索する（正規表現を無効にする）:

`grep {{[-F|--fixed-strings]}} "{{正確な文字列}}" {{path/to/file}}`

- ディレクトリ内の全てのファイルを再帰的にパターン検索し、マッチしたファイルの行番号を表示する:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{検索パターン}}" {{path/to/directory}}`

- 拡張正規表現 (`?`, `+`, `{}`, `()`, `|` をサポート)を大文字小文字を区別しないモードで使用する:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{検索パターン}}" {{path/to/file}}`

- 各マッチの前後3行のコンテキストを表示する:

`grep {{--context|--before-context|--after-context}} 3 "{{検索パターン}}" {{path/to/file}}`

- 各マッチのファイル名と行番号をカラー出力する:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{検索パターン}}" {{path/to/file}}`

- パターンにマッチする行を検索し、マッチしたテキストのみを表示する:

`grep {{[-o|--only-matching]}} "{{検索パターン}}" {{path/to/file}}`

- パターンにマッチしない行を `stdin` から検索する:

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{検索パターン}}"`
