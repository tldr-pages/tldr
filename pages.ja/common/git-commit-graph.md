# git commit-graph

> Gitのcommit-graphファイルを書き込み、検証する。
> 詳細情報: <https://git-scm.com/docs/git-commit-graph>。

- リポジトリのローカル `.git` ディレクトリ内にあるパック済みコミット用のcommit-graphファイルを書き込む:

`git commit-graph write`

- 到達可能なすべてのコミットを含むcommit-graphファイルを書き込む:

`git show-ref {{[-s|--hash]}} | git commit-graph write --stdin-commits`

- 現在のcommit-graphファイル内のすべてのコミットと、`HEAD` から到達可能なコミットを含むcommit-graphファイルを書き込む:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
