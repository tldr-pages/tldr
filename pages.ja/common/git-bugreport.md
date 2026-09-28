# git bugreport

> Gitのバグ報告に役立つテキストファイルを生成するため、システムとユーザーからデバッグ情報を取得する。
> 詳細情報: <https://git-scm.com/docs/git-bugreport>。

- 現在のディレクトリに新しいバグ報告ファイルを作成する:

`git bugreport`

- 指定したディレクトリに新しいバグ報告ファイルを作成し、存在しない場合はそのディレクトリを作成する:

`git bugreport {{[-o|--output-directory]}} {{ディレクトリ/サブディレクトリ}}`

- `strftime` 形式の指定したファイル名サフィックスで新しいバグ報告ファイルを作成する:

`git bugreport {{[-s|--suffix]}} {{%m%d%y}}`
