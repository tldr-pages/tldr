# snap

> 自己完結型の "snap" ソフトウェアパッケージを管理します。
> `apt` が `.deb` の為のものであるのと似ています。
> もっと詳しく: <https://manned.org/snap>。

- パッケージを検索する:

`snap find {{クエリ}}`

- パッケージをインストール:

`snap install {{パッケージ}}`

- パッケージを更新:

`snap refresh {{パッケージ}}`

- パッケージを別のチャンネルに更新 (track, risk, または branch):

`snap refresh {{パッケージ}} --channel={{チャンネル}}`

- 全てのパッケージを更新する:

`snap refresh`

- インストールされている snap ソフトウェアの基本情報を表示:

`snap list`

- パッケージをアンインストール:

`snap remove {{パッケージ}}`

- システムに最近の snap の変更がないか確認:

`snap changes`
