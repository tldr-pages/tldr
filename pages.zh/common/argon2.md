# argon2

> 计算 Argon2 加密哈希。
> 更多信息：<https://github.com/P-H-C/phc-winner-argon2#command-line-utility>。

- 使用默认参数计算密码和盐的哈希：

`echo "{{密码}}" | argon2 "{{盐文本}}"`

- 使用指定算法计算哈希：

`echo "{{密码}}" | argon2 "{{盐文本}}" -{{d|i|id}}`

- 显示没有额外信息的编码哈希输出：

`echo "{{密码}}" | argon2 "{{盐文本}}" -e`

- 使用给定的迭代次数、内存使用量和并行度参数计算哈希：

`echo "{{密码}}" | argon2 "{{盐文本}}" -t {{5}} -m {{20}} -p {{7}}`
