# git symbolic-ref

> 参照を保存するファイルを読み取り、変更、削除する。
> 詳細情報: <https://git-scm.com/docs/git-symbolic-ref>。

- 名前を指定して参照を保存する:

`git symbolic-ref refs/{{名前}} {{参照}}`

- 更新理由のメッセージを含め、名前を指定して参照を保存する:

`git symbolic-ref -m "{{メッセージ}}" refs/{{名前}} refs/heads/{{ブランチ名}}`

- 名前を指定して参照を読み取る:

`git symbolic-ref refs/{{名前}}`

- 名前を指定して参照を削除する:

`git symbolic-ref {{[-d|--delete]}} refs/{{名前}}`

- スクリプト用に `--quiet` でエラーを隠し、`--short` で簡潔にする ("refs/heads/X" は "X" と表示される):

`git symbolic-ref {{[-q|--quiet]}} --short refs/{{名前}}`
