# brew

> Homebrew - macOS と Linux 用のパッケージマネージャ。
> `install` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
> もっと詳しく: <https://docs.brew.sh/Manpage>。

- formulae や cask の最新の安定版をインストールする:

`brew install {{formula|cask}}`

- 全てのインストールされている formulae や cask を一覧表示:

`brew list`

- インストールされている formula または cask をアップグレード (何も指定されない場合、インストールされている全ての formulae/cask がアップグレードされる):

`brew upgrade {{formula|cask}}`

- Homebrew のソースリポジトリから、Homebrew の最新バージョン、全ての formulae と cask を取得:

`brew update`

- より新しいバージョンが利用可能な formulae と cask を表示:

`brew outdated`

- 利用可能な formulae (パッケージ) と cask (ネイティブ macOS の `.app` パッケージ) を検索:

`brew search {{検索文字列}}`

- formula または cask の情報を表示 (バージョン, インストールパス, 依存関係, etc.):

`brew info {{formula|cask}}`

- ローカルの Homebrew インストールに潜在的な問題がないかチェック:

`brew doctor`
