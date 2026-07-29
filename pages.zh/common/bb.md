# bb

> 用于脚本编写的原生 Clojure 解释器。
> 更多信息：<https://book.babashka.org/#usage>。

- 计算表达式：

`bb {{[-e|--eval]}} "(+ 1 2 3)"`

- 计算脚本文件：

`bb {{[-f|--file]}} {{路径/到/脚本.clj}}`

- 将输入绑定到 `stdin` 中的行序列：

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- 将输入绑定到 `stdin` 中的 EDN（可扩展数据表示法）值序列：

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
