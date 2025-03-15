# curl

> データをサーバーから転送、もしくはサーバーへ転送します。
> HTTP、FTP、POP3を含むほとんどのプロトコルをサポートしています。
> もっと詳しく: <https://curl.se/docs/manpage.html>。

- URLのコンテンツをファイルにダウンロードする:

`curl {{http://example.com}} {{[-o|--output]}} {{ファイルパス}}`

- ファイルをダウンロードし、URLにより指定されたファイル名で出力を保存する:

`curl {{[-O|--remote-name]}} {{http://example.com/filename}}`

- ファイルをダウンロードし、ロケーションレスポンスヘッダーのリダイレクトに追従しつつ自動的に以前のファイル転送を継続(再開)する。サーバーエラー時にはエラーを返す:

`curl {{[-f|--fail]}} {{[-O|--remote-name]}} {{[-L|--location]}} {{[-C|--continue-at]}} - {{http://example.com/filename}}`

- フォームエンコードされたデータを送信する（`application/x-www-form-urlencoded`型のPOSTリクエスト）。`stdin`(標準入力) から読み込むには、`--data @file_name` または `--data @'-'` を使用する:

`curl {{[-d|--data]}} {{'name=bob'}} {{http://example.com/form}}`

- カスタムHTTPメソッドを用いて追加のヘッダーを持つリクエストを送信する:

`curl {{[-H|--header]}} {{'X-My-Header: 123'}} {{[-X|--request]}} {{PUT}} {{http://example.com}}`

- 適切なContent-Type 表現ヘッダーを指定することで、JSONフォーマットでデータを送信する:

`curl {{[-d|--data]}} {{'{"name":"bob"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- サーバー認証のためユーザー名とパスワードを送る:

`curl {{[-u|--user]}} {{ユーザー名}} {{http://example.com}}`

- リソースのクライアント証明書とキーを送り、証明書の検証をスキップする:

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://example.com}}`
