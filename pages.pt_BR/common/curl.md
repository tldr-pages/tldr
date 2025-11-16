# curl

> Transfere dados entre o computador local e um servidor.
> Suporta a maioria dos protocolos de comunicação, incluindo HTTP, HTTPS, FTP, SCP, etc.
> Mais informações: <https://curl.se/docs/manpage.html>.

- Faz um pedido HTTP GET e descarrega os conteúdos em `stdout` (saída padrão):

`curl {{https://example.com}}`

- Faz um pedido HTTP GET, segue redirecionamentos `3xx` e descarrega os cabeçalhos da resposta e conteúdos para `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Baixa um arquivo, salvando a saída no arquivo indicado pela URL:

`curl {{[-O|--remote-name]}} {{https://example.com/arquivo.zip}}`

- Envia dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`). Usa `--data @file_name` ou `--data @'-'` para ler da `stdin`:

`curl {{[-X|--request]}} POST {{[-d|--data]}} {{'nome=maria'}} {{http://example.com/formulario}}`

- Envia um pedido com um cabeçalho adicional, usando um método HTTP personalizado e por meio de um proxy (tal como BurpSuite), ignorando certificados autoassinados inseguros:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} {{'Authorization: Bearer token'}} {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Envia dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl {{[-d|--data]}} {{'{"nome":"maria"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/usuarios/1234}}`

- Passa o certificado do cliente e chave para um recurso, pulando a validação do certificado:

`curl {{[-E|--cert]}} {{cliente.pem}} --key {{chave.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Resolve um hostname para um endereço de IP personalizado, com a saída verbosa (similar a editar o arquivo `/etc/hosts` para resolução de DNS personalizada):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
