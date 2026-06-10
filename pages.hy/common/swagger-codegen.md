# swagger-codegen

> Ստեղծեք կոդը և փաստաթղթերը ձեր REST api-ի համար OpenAPI/swagger սահմանումից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/swagger-api/swagger-codegen>:.

- Ստեղծեք փաստաթղթեր և կոդ OpenAPI/swagger ֆայլից.:

`swagger-codegen generate {{[-i|--input-spec]}} {{swagger_file}} {{[-l|--lang]}} {{language}}`

- Ստեղծեք Java կոդը՝ օգտագործելով գրադարանի retrofit2-ը և useRxJava2 տարբերակը:

`swagger-codegen generate {{[-i|--input-spec]}} {{http://petstore.swagger.io/v2/swagger.json}} {{[-l|--lang]}} {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}`

- Ցուցակեք մատչելի լեզուները.:

`swagger-codegen langs`

- Ցուցադրել օգնություն կոնկրետ հրամանի համար.:

`swagger-codegen {{generate|config-help|meta|langs|version}} --help`
