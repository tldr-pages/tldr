# git archive

> ツリーからファイルのアーカイブを作成する。
> 詳細情報: <https://git-scm.com/docs/git-archive>。

- 現在の `HEAD` の内容から `.tar` アーカイブを作成して `stdout` に出力する:

`git archive {{[-v|--verbose]}} HEAD`

- Zip形式を使用して進捗を詳細に表示する:

`git archive {{[-v|--verbose]}} --format zip HEAD`

- Zipアーカイブを指定したファイルへ出力する:

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{ディレクトリ/サブディレクトリ/ファイル.zip}} HEAD`

- 指定したブランチの最新コミットの内容から `.tar` アーカイブを作成する:

`git archive {{[-o|--output]}} {{ディレクトリ/サブディレクトリ/ファイル.tar}} {{ブランチ名}}`

- 指定したディレクトリの内容を使用する:

`git archive {{[-o|--output]}} {{ディレクトリ/サブディレクトリ/ファイル.tar}} HEAD:{{ディレクトリ/サブディレクトリ}}`

- 各ファイルのパスの先頭にパスを付加してアーカイブ内の指定したディレクトリに格納する:

`git archive {{[-o|--output]}} {{ディレクトリ/サブディレクトリ/ファイル.tar}} --prefix {{付加する/パス}}/ HEAD`
