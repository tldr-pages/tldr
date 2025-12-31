# ls

> ディレクトリの内容を一覧表示します。
> もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>。

- ファイルを1行ごとに一覧表示:

`ls -1`

- 隠しファイルを含むすべてのファイルを一覧表示:

`ls {{[-a|--all]}}`

- すべてのファイルを一覧表示し、ディレクトリ名の最後に `/` を付加する:

`ls {{[-F|--classify]}}`

- 全ファイルを長い形式（パーミッション、所有者、サイズ、修正日）で一覧表示します:

`ls {{[-la|--all -l]}}`

- サイズを人間が読みやすい単位（KiB、MiB、GiB）で表示した長い形式での一覧表示:

`ls {{[-lh|-l --human-readable]}}`

- サイズ順（降順）に並べた長い形式での一覧表示:

`ls {{-lSR|-lS --recursive}}`

- すべてのファイルの長い形式でのリストで、更新日が古いものから順に表示されます:

`ls {{[-ltr|-lt --reverse]}}`
