# curl

> Transfere dados entre o computador local e um servidor.
> Suporta a maioria dos protocolos de comunicação, incluindo HTTP, HTTPS, FTP, SCP, etc.
> Mais informações: <https://curl.se/docs/manpage.html>.

- Faz um pedido HTTP GET e descarrega os conteúdos em `stdout` (saída padrão):

`curl {{https://example.com}}`

- Faz um pedido HTTP GET, segue redirecionamentos ``3xx` e descarrega os cabeçalhos da resposta e conteúdos para `stdout`:

`curl --location --dump-header - {{https://example.com}}`

- Baixa um arquivo, salvando a saída no arquivo indicado pela URL:

`curl --remote-name {{https://example.com/arquivo.zip}}`

- Envia dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`). Usa `--data @file_name` ou `--data @'-'` para ler da `stdin`:

`curl -X POST --data {{'nome=maria'}} {{http://example.com/formulario}}`

- Envia um pedido com um cabeçalho adicional, usando um método HTTP personalizado e por meio de um proxy (tal como BurpSuite), ignorando certificados autoassinados inseguros:

`curl -k --proxy {{http://127.0.0.1:8080}} --header {{'Authorization: Bearer token'}} --request {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Envia dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl --data {{'{"nome":"maria"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/usuarios/1234}}`

- Passa o certificado do cliente e chave para um recurso, pulando a validação do certificado:

`curl --cert {{cliente.pem}} --key {{chave.pem}} --insecure {{https://example.com}}`

- Resolve um hostname para um endereço de IP personalizado, com a saída verbosa (similar a editar o arquivo `/etc/hosts` para resolução de DNS personalizada):

`curl --verbose --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
