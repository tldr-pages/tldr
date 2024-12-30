# jwt

> 处理 JSON Web Tokens (JWT)。
> 可用的加密算法有 HS256、HS384、HS512、RS256、RS384、RS512、ES256、ES384。
> 更多信息：<https://github.com/mike-engel/jwt-cli>。

- 解码 JWT：

`jwt decode {{jwt_string}}`

- 将 JWT 解码为 JSON 字符串：

`jwt decode -j {{jwt_string}}`

- 将 JSON 字符串编码为 JWT：

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_string}}'`

- 将密钥对有效负载编码为 JWT：

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P {{key=value}}`