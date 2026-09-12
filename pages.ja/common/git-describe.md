# git describe

> 利用可能な参照を基に、オブジェクトへ人間が読める名前を付ける。
> 詳細情報: <https://git-scm.com/docs/git-describe>。

- 現在のコミットに一意な名前を作成する (名前には最新の注釈付きタグ、追加コミット数、短縮コミットハッシュが含まれる):

`git describe`

- 短縮コミットハッシュを4桁にした名前を作成する:

`git describe --abbrev={{4}}`

- タグ参照パスを含む名前を生成する:

`git describe --all`

- Gitタグの名前を生成する:

`git describe {{v1.0.0}}`

- 指定したブランチの最新コミットの名前を作成する:

`git describe {{ブランチ名}}`
