# rustup

> Rust ツールチェーンのインストール、管理、更新を行います。
> `toolchain`, `target`, `update` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://rust-lang.github.io/rustup>。

- nightly ツールチェーンをシステムにインストール:

`rustup install nightly`

- デフォルトのツールチェーンを nightly に切り替えて、`cargo` コマンドと `rustc` コマンドがそれを使用するようにする:

`rustup default nightly`

- 現在のプロジェクト内では nightly ツールチェーンを使用するが、グローバル設定は変更しない:

`rustup override set nightly`

- 全てのツールチェーンを更新:

`rustup update`

- インストール済ツールチェーンを一覧表示:

`rustup show`

- 特定のツールチェーンで `cargo build` を実行:

`rustup run {{ツールチェーン名}} cargo build`

- デフォルトのウェブブラウザでローカルの Rust ドキュメントを開く:

`rustup doc`
