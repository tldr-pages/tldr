# jwt

> Uma ferramenta de linha de comando (command-line tool) para trabalhar com JSON Web Tokens (JWTs).
> Algoritmos de encriptação disponíveis são HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
> Mais informações: <https://github.com/mike-engel/jwt-cli>.

- Decodifica um JWT:

`jwt decode {{jwt_string}}`

- Decodifica um JWT em uma JSON string:

`jwt decode -j {{jwt_string}}`

- Codifica uma JSON string em um JWT:

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_string}}'`

- Codifica dados (payload) de um par de chaves (key pair) em um JWT:

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P {{chave=valor}}`
