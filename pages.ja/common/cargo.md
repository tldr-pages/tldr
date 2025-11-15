# cargo

> Rust プロジェクトとそのモジュールの依存関係(クレート)を管理します。
> `build` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://doc.rust-lang.org/cargo>。

- クレートを検索:

`cargo search {{検索文字列}}`

- バイナリのクレートをインストール:

`cargo install {{クレート名}}`

- インストールされたバイナリクレートを一覧表示:

`cargo install --list`

- 指定したディレクトリ（デフォルトでは現在の作業ディレクトリ）に新しいバイナリまたはライブラリ Rust プロジェクトを作成:

`cargo init --{{bin|lib}} {{path/to/directory}}`

- カレントディレクトリの `Cargo.toml` に依存関係を追加:

`cargo add {{dependency}}`

- カレントディレクトリの Rust プロジェクトを release プロファイルを使ってビルド:

`cargo {{[b|build]}} {{[-r|--release]}}`

- nightly コンパイラを使ってカレントディレクトリに Rust プロジェクトをビルド (`rustup` が必要):

`cargo +nightly {{[b|build]}}`

- 特定のスレッド数を使用してビルド (デフォルトは論理 CPU 数):

`cargo {{[b|build]}} --jobs {{スレッド数}}`
