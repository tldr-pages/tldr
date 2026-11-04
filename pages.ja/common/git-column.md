# git column

> データを列形式で表示する。
> 詳細情報: <https://git-scm.com/docs/git-column>。

- `stdin` を複数の列に整形する:

`ls | git column --mode={{column}}`

- `stdin` を最大幅 `100` の複数の列に整形する:

`ls | git column --mode=column --width={{100}}`

- `stdin` を最大余白 `30` の複数の列に整形する:

`ls | git column --mode=column --padding={{30}}`
