# git check-ref-format

> 参照名が許容される形式か確認し、許容されない場合は0以外のステータスで終了する。
> 詳細情報: <https://git-scm.com/docs/git-check-ref-format>。

- 指定した参照名の形式を確認する:

`git check-ref-format {{refs/head/refname}}`

- 最後にチェックアウトしたブランチ名を出力する:

`git check-ref-format --branch @{-1}`

- 参照名を正規化する:

`git check-ref-format --normalize {{refs/head/refname}}`
