# apt

> Debian系ディストリビューションで使われるパッケージ管理システムです。
> Ubuntuのバージョンが16.04か、それ以降で対話モードを使う場合`apt-get`の代わりとして使用します。
> 詳しくはこちら: <https://manpages.debian.org/latest/apt/apt.8.html>

- 利用可能なパーケージとバージョンのリストの更新（他の`apt`コマンドの前での実行を推奨）:

`sudo apt update`

- 指定されたパッケージの検索:

`apt search {{パッケージ}}`

- パッケージの情報を出力:

`apt show {{パッケージ}}`

- パッケージのインストール、または利用可能な最新バージョンに更新:

`sudo apt install {{パッケージ}}`

- パッケージの削除（`sudo apt remove --purge`の場合設定ファイルも削除）:

`sudo apt remove {{パッケージ}}`

- インストールされている全てのパッケージを最新のバージョンにアップグレード:

`sudo apt upgrade`

- インストールできるすべてのパッケージを表示:

`apt list`

- インストールされた全てのパッケージを表示（依存関係も表示）:

`apt list --installed`
