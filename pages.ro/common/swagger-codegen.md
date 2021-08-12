# swagger-codegen

> Generați cod și documentație pentru API REST dintr-o definiție OpenAPI/Swagger.
> Mai multe informaţii: <https://github.com/swagger-api/swagger-codegen>

- Generați documentația și codul dintr-un fișier OpenAPI/Swagger:

`swagger-codegen generate -i {{swagger_file}} -l {{language}}`

- Generarea codului Java folosind biblioteca retrofit2 și opțiunea UserXjava2:

`swagger-codegen generate -i {{http://petstore.swagger.io/v2/swagger.json}} -l {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}`

- Lista limbilor disponibile:

`swagger-codegen langs`

- Afișați opțiunile de ajutor pentru comanda generare:

`swagger-codegen help {{generate}}`
