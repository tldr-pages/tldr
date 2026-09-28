# git switch

> Gitブランチを切り替える。Git 2.23以降が必要。
> 参照: `git checkout`。
> 詳細情報: <https://git-scm.com/docs/git-switch>。

- 既存のブランチに切り替える:

`git switch {{ブランチ名}}`

- 新しいブランチを作成して切り替える:

`git switch {{[-c|--create]}} {{ブランチ名}}`

- 既存のコミットを基に新しいブランチを作成して切り替える:

`git switch {{[-c|--create]}} {{ブランチ名}} {{コミット}}`

- 直前のブランチに切り替える:

`git switch -`

- ブランチへ切り替え、すべてのサブモジュールも一致するように更新する:

`git switch --recurse-submodules {{ブランチ名}}`

- ブランチへ切り替え、現在のブランチと未コミットの変更を自動的にマージする:

`git switch {{[-m|--merge]}} {{ブランチ名}}`

- タグまたはコミットに切り替える:

`git switch {{[-d|--detach]}} {{タグ|コミット}}`

- 別のリモートにあるブランチへ切り替える:

`git switch {{[-t|--track]}} {{リモート名}}/{{ブランチ}}`
