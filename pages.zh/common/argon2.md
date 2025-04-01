# argon2

> 计算 Argon2 密码哈希。
> 更多信息：<https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- 使用默认参数计算带有密码和盐的哈希：

`echo "{{password}}" | argon2 "{{salt_text}}"`

- 使用指定的算法计算哈希：

`echo "{{password}}" | argon2 "{{salt_text}}" -{{d|i|id}}`

- 仅显示输出哈希，不显示其他信息：

`echo "{{password}}" | argon2 "{{salt_text}}" -e`

- 使用给定的迭代次数 [t]、内存使用量 [m] 和并行度 [p] 参数计算哈希：

`echo "{{password}}" | argon2 "{{salt_text}}" -t {{5}} -m {{20}} -p {{7}}`
