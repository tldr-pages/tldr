# npm

> JavaScript と Node.js のパッケージマネージャ。
> Node.js プロジェクトとそのモジュールの依存関係を管理します。
> 詳細情報: <https://docs.npmjs.com/cli/npm/>。

- デフォルト値の `package.json` ファイルを生成 (対話的に行う場合は `--yes` を省略):

`npm init {{[-y|--yes]}}`

- `package.json`に依存パッケージとしてリストされている全てのパッケージをダウンロード:

`npm {{[i|install]}}`

- パッケージの特定のバージョンをダウンロードして `package.json` の dependencies に追加:

`npm {{[i|install]}} {{パッケージ名}}@{{バージョン}}`

- パッケージの最新バージョンをダウンロードして `package.json` の dev dependencies に追加:

`npm {{[i|install]}} {{パッケージ名}} {{[-D|--save-dev]}}`

- パッケージの最新バージョンをダウンロードし、グローバルにインストール:

`npm {{[i|install]}} {{パッケージ名}} {{[-g|--global]}}`

- パッケージをアンインストールして `package.json` の dependencies から削除:

`npm {{[r|uninstall]}} {{パッケージ名}}`

- ローカルにインストールされている依存パッケージを全て一覧表示:

`npm {{[ls|list]}}`

- グローバルにインストールされているトップレベルのパッケージを一覧表示する:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
