# jwt

> A JSON webes tokenekkel (JWT-k) dolgozó parancssori eszköz. A következő titkosítási algoritmusok állnak rendelkezésre: HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384. További információ: <https://github.com/mike-engel/jwt-cli>.

- JWT dekódolása:

`jwt decode {{jwt_string}}`

- A JWT dekódolása JSON-stringként:

`jwt decode -j {{jwt_string}}`

- Egy JSON karakterlánc JWT-be kódolása:

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_string}}'`

- Kulcspár hasznos terhelésének kódolása JWT-be:

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P key=value`
