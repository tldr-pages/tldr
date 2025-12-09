# tee

> `stdin` から読み込んで `stdout` とファイル(またはコマンド)に書き込みます。
> もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>。

- 各ファイルに `stdin` をコピーし、`stdout` にもコピーする:

`echo "example" | tee {{path/to/file}}`

- 与えられたファイルに追記する。上書きはしない:

`echo "example" | tee {{[-a|--append]}} {{path/to/file}}`

- ターミナルに `stdin` を表示し、さらに処理するために別のプログラムにパイプする:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- "example"と言うディレクトリを作成し、"example"の文字バイト数を数え、"example"をターミナルに出力する:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
