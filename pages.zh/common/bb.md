# bb

> 用于脚本的原生 Clojure 解释器。
> 更多信息：<https://book.babashka.org/#usage>。

- [e]valuate 表达式：

`bb -e "(+ 1 2 3)"`

- 评估脚本 [f]ile：

`bb -f {{path/to/script.clj}}`

- 将 [i]nput 绑定为来自 `stdin` 的一系列行：

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- 将 [I]nput 绑定为来自 `stdin` 的一系列 EDN（可扩展数据标记）值：

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`