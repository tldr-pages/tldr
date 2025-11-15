# jwt

> 使用 JSON Web Tokens (JWTs) 进行操作。
> 可用的加密算法包括 HS256、HS384、HS512、RS256、RS384、RS512、ES256、ES384。
> 更多信息：<https://github.com/mike-engel/jwt-cli>.

- 解码一个 JWT：

`jwt decode {{jwt字符串}}`

- 将 JWT 解码为 JSON 字符串：

`jwt decode -j {{jwt字符串}}`

- 将 JSON 字符串编码为 JWT：

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json字符串}}'`

- 将键值对载荷编码为 JWT：

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P {{键=值}}`
