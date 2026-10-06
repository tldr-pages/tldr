# git cvsexportcommit

> 1つのGitコミットをCVSのチェックアウトへエクスポートする。
> 詳細情報: <https://git-scm.com/docs/git-cvsexportcommit>。

- 指定したパッチをCVSへマージする:

`git cvsexportcommit -v -c -w {{CVSプロジェクトのチェックアウト先パス}} {{コミットSHA1}}`
