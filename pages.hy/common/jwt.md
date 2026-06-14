#jwt

> Աշխատեք JSON Web Tokens-ի հետ (JWT):.
> Գաղտնագրման ալգորիթմներն են՝ HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mike-engel/jwt-cli>:.

- Վերծանել JWT:

`jwt decode {{jwt_string}}`

- Վերծանեք JWT-ը որպես JSON տող.:

`jwt decode {{[-j|--json]}} {{jwt_string}}`

- JSON տողը կոդավորեք JWT-ում.:

`jwt encode {{[-A|--alg]}} {{HS256}} {{[-S|--secret]}} {{1234567890}} '{{json_string}}'`

- Կոդավորեք առանցքային զույգի օգտակար բեռը JWT-ին.:

`jwt encode {{[-A|--alg]}} {{HS256}} {{[-S|--secret]}} {{1234567890}} {{[-P|--payload]}} {{key=value}}`
