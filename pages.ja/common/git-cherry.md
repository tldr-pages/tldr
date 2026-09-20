# git cherry

> まだ上流に適用されていないコミットを見つける。
> 詳細情報: <https://git-scm.com/docs/git-cherry>。

- 上流に同等のコミットがあるコミットとそのメッセージを表示する:

`git cherry {{[-v|--verbose]}}`

- 別の上流ブランチとトピックブランチを指定する:

`git cherry {{origin}} {{topic}}`

- コミットを指定した範囲内のものに制限する:

`git cherry {{origin}} {{topic}} {{base}}`
