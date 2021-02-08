# curl

> Transfere dados entre o computador local e um servidor remoto.
> Suporta a maioria dos protocolos de comunicação, incluindo HTTP, FTP e POP3.
> Mais informações: <https://curl.se>.

- Descarregar os conteúdos de um URL para um arquivo:

`curl {{http://example.com}} -o {{arquivo}}`

- Descarregar um arquivo, gravando o resultado sob o nome do arquivo indicado pelo URL:

`curl -O {{http://example.com/arquivo}}`

- Descarregar um arquivo, seguindo redirecionamentos e automaticamente continuando transferências idênticas que tenham sido interrompidas:

`curl -O -L -C - {{http://example.com/arquivo}}`

- Enviar dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`):

`curl -d {{'nome=maria'}} {{http://example.com/formulario}}`

- Enviar um pedido com um cabeçalho adicional, usando um método HTTP personalizado:

`curl -H {{'X-Meu-Cabecalho: 123'}} -X {{PUT}} {{http://example.com}}`

- Enviar dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl -d {{'{"nome":"maria"}'}} -H {{'Content-Type: application/json'}} {{http://example.com/usuarios/123}}`

- Passar ao pedido o nome de usuário e senha para autenticação no servidor:

`curl -u usuario:senha {{http://example.com}}`

- Passar ao pedido o certificado do cliente e a chave para um recurso, omitindo a validação do certificado:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
