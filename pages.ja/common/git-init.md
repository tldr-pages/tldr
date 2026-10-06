# git init

> 新しいローカルGitリポジトリを初期化する。
> 詳細情報: <https://git-scm.com/docs/git-init>。

- 新しいローカルリポジトリを初期化する:

`git init`

- 初期ブランチの名前を指定してリポジトリを初期化する:

`git init {{[-b|--initial-branch]}} {{ブランチ名}}`

- オブジェクトのハッシュにSHA256を使用してリポジトリを初期化する (Git 2.29以降が必要):

`git init --object-format sha256`

- SSH経由のリモートとしての使用に適した、作業ツリーのないリポジトリを初期化する:

`git init --bare`
