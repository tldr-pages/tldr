# git request-pull

> 上流プロジェクトに変更を取り込むよう依頼するリクエストを生成する。
> 詳細情報: <https://git-scm.com/docs/git-request-pull>。

- v1.1リリースと指定したブランチの間の変更を要約するリクエストを生成する:

`git request-pull {{v1.1}} {{https://example.com/project}} {{ブランチ名}}`

- `foo` ブランチ上のv0.1リリースとローカルの `bar` ブランチの間の変更を要約するリクエストを生成する:

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`
