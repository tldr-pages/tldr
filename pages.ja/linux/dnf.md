# dnf

> RHEL、Fedora、CentOS 用のパッケージ管理ユーティリティ (yum の後継)。
> `group`, `config-manager` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> 他のパッケージマネジャーの同等のコマンドについては、 <https://wiki.archlinux.org/title/Pacman/Rosetta> を参照してください。
> もっと詳しく: <https://dnf.readthedocs.io/en/latest/command_ref.html>。

- インストールされたパッケージを、利用可能な最新バージョンにアップグレードする:

`sudo dnf upgrade`

- キーワードでパッケージを検索:

`dnf search {{キーワード1 キーワード2 ...}}`

- パッケージの詳細を表示:

`dnf info {{パッケージ}}`

- 新しいパッケージをインストール (`-y` を使用すると、全てのプロンプトを自動的に追認する):

`sudo dnf install {{パッケージ1 パッケージ2 ...}}`

- パッケージを削除:

`sudo dnf remove {{パッケージ1 パッケージ2 ...}}`

- インストールされているパッケージを一覧表示:

`dnf list --installed`

- 指定したコマンドを提供するパッケージを検索:

`dnf provides {{コマンド}}`

- 過去の全オペレーションを見る:

`dnf history`
