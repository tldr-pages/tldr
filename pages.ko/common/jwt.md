# jwt

> JSON Web Token(JWT) 처리.
> 사용할 수 있는 암호화 알고리즘: HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
> 더 많은 정보: <https://github.com/mike-engel/jwt-cli>.

- JWT 디코드:

`jwt decode {{jwt_문자열}}`

- JWT를 JSON 문자열로 디코드:

`jwt decode -j {{jwt_문자열}}`

- JSON 문자열을 JWT로 인코드:

`jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_문자열}}'`

- 키-값 쌍 페이로드를 JWT로 인코드:

`jwt encode --alg {{HS256}} --secret {{1234567890}} -P {{키=값}}`
