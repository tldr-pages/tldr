# git mktree

> `ls-tree` 形式のテキストを使ってツリーオブジェクトを構築する。
> 詳細情報: <https://git-scm.com/docs/git-mktree>。

- ツリーオブジェクトを構築し、各ツリーエントリのハッシュが既存オブジェクトを指していることを検証する:

`git mktree`

- 欠落したオブジェクトを許可する:

`git mktree --missing`

- ツリーオブジェクトのNUL終端出力 (`git ls-tree -z`) を読み取る:

`git mktree -z`

- 複数のツリーオブジェクトの作成を許可する:

`git mktree --batch`

- `stdin` から読み取った内容を並べ替えてツリーを構築する (非再帰の `git ls-tree` 出力形式が必要):

`git < {{ディレクトリ/サブディレクトリ/tree.txt}} mktree`
