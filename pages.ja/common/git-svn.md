# git svn

> SubversionリポジトリとGitの間で双方向に操作する。
> 詳細情報: <https://git-scm.com/docs/git-svn>。

- SVNリポジトリをクローンする:

`git svn clone {{https://example.com/subversion_repo}} {{ローカルディレクトリ}}`

- 指定したリビジョン番号からSVNリポジトリをクローンする:

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{ローカルディレクトリ}}`

- リモートSVNリポジトリからローカルクローンを更新する:

`git svn rebase`

- Gitの `HEAD` を変更せずにリモートSVNリポジトリから更新を取得する:

`git svn fetch`

- SVNリポジトリへコミットを戻す:

`git svn commit`
