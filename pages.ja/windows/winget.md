# winget

> Windows パッケージマネージャ。
> もっと詳しく: <https://learn.microsoft.com/windows/package-manager/winget>。

- パッケージをインストール:

`winget install {{パッケージ}}`

- パッケージを削除 (注意: `uninstall` の代わりに `remove` を使用することもできる):

`winget uninstall {{パッケージ}}`

- パッケージに関する情報を表示:

`winget show {{パッケージ}}`

- パッケージを検索:

`winget search {{パッケージ}}`

- 全てのパッケージを最新バージョンにアップグレード:

`winget upgrade --all`

- `winget`で管理可能なインストール済パッケージを全て一覧表示:

`winget list --source winget`

- ファイルからのパッケージのインポート、またはインストールされたパッケージのファイルへのエクスポート:

`winget {{import|export}} {{--import-file|--output}} {{path/to/file}}`

- winget-pkgs リポジトリに PR を開く前にマニフェストを検証する:

`winget validate {{path/to/manifest}}`
