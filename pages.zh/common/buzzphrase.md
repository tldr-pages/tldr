# 流行语

> 输出一个随机的流行语。使用 Node.js 编写。
> 更多信息：<https://github.com/atomantic/buzzphrase>。

- 生成一个包含形容词、过去式动词和复数名词的三个随机短语的字符串：

`buzzphrase`

- 打印格式为 [i]祈使动词 + 过去式 [v]动词 + [a]形容词 + 复数 [N]名词的短语：

`buzzphrase {{'{i} {v} {a} {N}'}}`

- 打印格式为现在分词 [V]动词 + [a]形容词 + 单数 [n]名词 + [f]结尾的 `k` 个短语：

`buzzphrase {{k}} {{'{V} {a} {n} {f}'}}`