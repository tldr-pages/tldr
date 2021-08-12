# jwt

> Un instrument de linie de comandă pentru a lucra cu JSON Web token-uri (JWT).
> Algoritmii de criptare disponibili sunt HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
> Mai multe informaţii: <https://github.com/mike-engel/jwt-cli>

- decodează un JWT:

`jwt decode {{jwt_string}}`

- decodează un JWT ca șir JSON:

`jwt decode -j {{jwt_string}}`

- Codifică un șir JSON la un JWT:

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_string}}'`

- Codifică sarcina utilă a perechii cheie la JWT:

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P key=value`
