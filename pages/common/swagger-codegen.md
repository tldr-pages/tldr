# swagger-codegen

> Generate code and documentation for your REST api from a OpenAPI/swagger definition.
> More information: <https://github.com/swagger-api/swagger-codegen>.

- Generate documentation and code from an OpenAPI/swagger file:

`swagger-codegen generate -i {{swagger_file}} -l {{language}}`

- Generate Java code using the library retrofit2 and the option useRxJava2:

`swagger-codegen generate -i {{http://petstore.swagger.io/v2/swagger.json}} -l {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}`

- List available languages:

`swagger-codegen langs`

- Display help options for the generate command:

`swagger-codegen help {{generate}}`
