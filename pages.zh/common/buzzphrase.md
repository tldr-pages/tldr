# buzzphrase

> 输出一个随机的专业术语短语。使用 Node.js 编写。
> 更多信息：<https://github.com/atomantic/buzzphrase>.

- 生成一个包含形容词、过去式动词和复数名词的三个随机短语的字符串：

`buzzphrase`

- 以 [i]命令式动词 + 过去式[v]动词 + [a]形容词 + 复数[N]名词 的格式打印短语：

`buzzphrase {{'{i} {v} {a} {N}'}}`

- 以现在分词[V]动词 + [a]形容词 + 单数[n]名词 + [f]结尾 的格式打印 `k` 个短语：

`buzzphrase {{k}} {{'{V} {a} {n} {f}'}}`