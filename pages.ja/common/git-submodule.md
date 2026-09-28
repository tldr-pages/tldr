# git submodule

> サブモジュールを確認・更新・管理する。
> 詳細情報: <https://git-scm.com/docs/git-submodule>。

- 既存のサブモジュールと各サブモジュールでチェックアウトされているコミットを表示する:

`git submodule`

- リポジトリのサブモジュール (`.gitmodules` に記載されたもの) をインストールする:

`git submodule update --init --recursive`

- Gitリポジトリを現在のリポジトリのサブモジュールとして追加する:

`git submodule add {{リポジトリURL}}`

- Gitリポジトリを指定したディレクトリに現在のリポジトリのサブモジュールとして追加する:

`git submodule add {{リポジトリURL}} {{ディレクトリ/サブディレクトリ}}`

- サブモジュールを最新のコミットに更新する:

`git submodule update --remote`

- サブモジュールのURLを変更する:

`git submodule set-url {{ディレクトリ/サブディレクトリ/サブモジュール}} {{新しいURL}}`

- サブモジュールの登録を解除する (例: `git rm` でリポジトリから削除する前):

`git submodule deinit {{ディレクトリ/サブディレクトリ/サブモジュール}}`
