# git count-objects

> 未パックのオブジェクト数と、そのディスク使用量を数える。
> 詳細情報: <https://git-scm.com/docs/git-count-objects>。

- すべてのオブジェクトを数え、合計ディスク使用量を表示する:

`git count-objects`

- すべてのオブジェクト数と合計ディスク使用量を、人間が読みやすい単位で表示する:

`git count-objects {{[-H|--human-readable]}}`

- より詳細な情報を表示する:

`git count-objects {{[-v|--verbose]}}`

- より詳細な情報を、人間が読みやすい単位で表示する:

`git count-objects {{[-H|--human-readable]}} {{[-v|--verbose]}}`
