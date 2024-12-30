# argon2

> 计算 Argon2 加密哈希。
> 更多信息：<https://github.com/P-H-C/phc-winner-argon2#command-line-utility>。

- 使用默认参数计算带有密码和盐的哈希：

`echo "{{password}}" | argon2 "{{salt_text}}"`

- 使用指定算法计算哈希：

`echo "{{password}}" | argon2 "{{salt_text}}" -{{d|i|id}}`

- 显示输出哈希而不附加信息：

`echo "{{password}}" | argon2 "{{salt_text}}" -e`

- 使用给定的迭代 [t] 次，内存使用 [m] 和并行参数 [p] 计算哈希：

`echo "{{password}}" | argon2 "{{salt_text}}" -t {{5}} -m {{20}} -p {{7}}`