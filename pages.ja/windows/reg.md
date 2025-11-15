# reg

> Windows レジストリのキーとその値を管理します。
> `add` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg>。

- レジストリのコマンドを実行する:

`reg {{command}}`

- サブキーの追加とコピーのドキュメントを見る:

`tldr reg {{add|copy}}`

- キーとサブキーの削除に関するドキュメントを見る:

`tldr reg {{delete|unload}}`

- キーの検索、表示、比較に関するドキュメントを見る:

`tldr reg {{compare|query}}`

- キーの所有権とACLを保持しないレジストリキーのエクスポートと、インポートに関するドキュメントを見る:

`tldr reg {{export|import}}`

- キーの所有権とACLを保持したまま、レジストリを保存、リストア、アンロードするためのドキュメントを見る:

`tldr reg {{save|restore|load|unload}}`

- ヘルプを表示する:

`reg /?`

- コマンドのヘルプを表示する:

`reg {{command}} /?`
