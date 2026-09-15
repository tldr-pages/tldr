# git shortlog

> `git log` の出力を要約する。
> 詳細情報: <https://git-scm.com/docs/git-shortlog>。

- 作成されたすべてのコミットの要約を、作成者名のアルファベット順にグループ化して表示する:

`git shortlog`

- 作成されたすべてのコミットの要約を、コミット数順に並べて表示する:

`git shortlog {{[-n|--numbered]}}`

- 作成されたすべてのコミットの要約を、コミッターの識別情報 (名前とメールアドレス) ごとにグループ化して表示する:

`git shortlog {{[-c|--committer]}}`

- 直近5コミットの要約を表示する (つまりリビジョン範囲を指定する):

`git shortlog HEAD~5..HEAD`

- 現在のブランチ内のすべてのユーザー、メールアドレス、コミット数を表示する:

`git shortlog {{[-sne|--summary --numbered --email]}}`

- すべてのブランチ内のすべてのユーザー、メールアドレス、コミット数を表示する:

`git shortlog {{[-sne|--summary --numbered --email]}} --all`
