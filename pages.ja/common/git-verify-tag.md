# git verify-tag

> タグのGPG検証を確認する。
> タグが署名されていない場合はエラーが発生する。
> 詳細情報: <https://git-scm.com/docs/git-verify-tag>。

- タグのGPG署名を確認する:

`git verify-tag {{タグ1 省略可能なタグ2 ...}}`

- タグのGPG署名を確認し、各タグの詳細を表示する:

`git verify-tag {{タグ1 省略可能なタグ2 ...}} {{[-v|--verbose]}}`

- タグのGPG署名を確認し、生の詳細を出力する:

`git verify-tag {{タグ1 省略可能なタグ2 ...}} --raw`
