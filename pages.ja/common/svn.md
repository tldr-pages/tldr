# svn

> Subversion のコマンドラインクライアントツールです。
> 詳細情報: <https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn>。

- リポジトリから作業コピーをチェックアウトする:

`svn {{[co|checkout]}} {{url/to/repository}}`

- リポジトリからの変更を作業コピーに取り込む:

`svn {{[up|update]}}`

- ファイルやディレクトリをバージョン管理下に置き、リポジトリへの追加をスケジューリングする。これらは次のコミットで追加される:

`svn add {{パス}}`

- 作業コピーの変更をリポジトリに送信する:

`svn {{[ci|commit]}} {{[-m|--message]}} {{コミットログメッセージ}} [{{パス}}]`

- 過去10リビジョンの変更点を表示し、各リビジョンで変更されたファイルを表示する:

`svn log {{[-vl|--verbose --limit]}} {{10}}`

- ヘルプを表示する:

`svn {{[h|help]}}`
