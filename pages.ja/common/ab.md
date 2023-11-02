# ab

> Apache HTTP server のベンチマーク用ツールです。
> 詳しくはこちら: <https://httpd.apache.org/docs/current/programs/ab.html>

- 指定された URL に 100 個の GET リクエストを送信する:

`ab -n {{100}} {{url}}`

- 指定された URL に 100 個の GET リクエストを、10 個ずつ同時に送信する:

`ab -n {{100}} -c {{10}} {{url}}`

- ファイルからの JSON ペイロードを使って、指定された URL に 100 個の POST リクエストを送信する:

`ab -n {{100}} -T {{application/json}} -p {{ファイルパス.json}} {{url}}`

- [K]eep Alive を有効化する（１つの HTTP セッションで複数のリクエストを実行する）:

`ab -k {{url}}`

- ベンチマークを行う最大秒数を設定する:

`ab -t {{60}} {{url}}`
