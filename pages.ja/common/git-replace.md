# git replace

> オブジェクトを置き換える参照を作成、一覧表示、削除する。
> 詳細情報: <https://git-scm.com/docs/git-replace>。

- 他のコミットを変更せず、任意のコミットを別のコミットで置き換える:

`git replace {{オブジェクト}} {{置換先}}`

- 指定したオブジェクトに対する既存のreplace参照を削除する:

`git replace {{[-d|--delete]}} {{オブジェクト}}`

- オブジェクトの内容を対話的に編集する:

`git replace --edit {{オブジェクト}}`
