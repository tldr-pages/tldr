# argon2

> 计算 Argon2 加密哈希值。
> 更多信息：<https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- 使用默认参数，通过密码和盐值计算哈希：

`echo "{{密码}}" | argon2 "{{盐值文本}}"`

- 使用指定的算法计算哈希：

`echo "{{密码}}" | argon2 "{{盐值文本}}" -{{d|i|id}}`

- 显示不包含附加信息的 [e] 编码哈希输出：

`echo "{{密码}}" | argon2 "{{盐值文本}}" -e`

- 使用指定的迭代 [t] 次数、[m] 内存使用量和 [p] 并行度参数计算哈希：

`echo "{{密码}}" | argon2 "{{盐值文本}}" -t {{5}} -m {{20}} -p {{7}}`
