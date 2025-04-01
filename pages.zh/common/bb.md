# bb

> Clojure 脚本的原生解释器。
> 更多信息：<https://book.babashka.org/#usage>。

- 评估一个表达式：

`bb {{[-e|--eval]}} "(+ 1 2 3)"`

- 评估一个脚本文件：

`bb {{[-f|--file]}} {{path/to/script.clj}}`

- 将 [i] 输入绑定到从 `stdin` 读取的行序列：

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- 将 [I] 输入绑定到从 `stdin` 读取的 EDN（扩展数据表示法）值序列：

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`
