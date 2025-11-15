# node

> サーバサイド JavaScript プラットフォーム (Node.js)。
> もっと詳しく: <https://nodejs.org>。

- JavaScript ファイルを実行:

`node {{path/to/file}}`

- REPL(インタラクティブシェル)を開始:

`node`

- インポートされたファイルが変更された時に、プロセスを再起動して指定されたファイルを実行する (Node.js version 18.11+ が必要):

`node --watch {{path/to/file}}`

- JavaScript コードを引数として渡して評価する:

`node {{[-e|--eval]}} "{{code}}"`

- 結果を評価して表示する。ノードの依存関係のバージョンを出力するのに役立つ:

`node {{[-p|--print]}} "process.versions"`

- ソースコードが完全に解析されたら、デバッガが接続されるまで実行を一時停止するインスペクタをアクティブにする:

`node --no-lazy --inspect-brk {{path/to/file}}`
