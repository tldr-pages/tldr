# curl

> Transfere dados entre o computador local e um servidor remoto.
> Suporta a maioria dos protocolos de comunicação, incluindo HTTP, FTP e POP3.
> Mais informações: <https://curl.se/docs/manpage.html>.

- Descarrega os conteúdos de um URL para um arquivo:

`curl {{http://example.com}} --output {{arquivo}}`

- Descarrega um arquivo, gravando o resultado sob o nome do arquivo indicado pelo URL:

`curl --remote-name {{http://example.com/arquivo}}`

- Descarrega um arquivo, seguindo redirecionamentos e automaticamente continuando transferências idênticas que tenham sido interrompidas:

`curl --fail --remote-name --location --continue-at - {{http://example.com/arquivo}}`

- Envia dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`):

`curl --data {{'nome=maria'}} {{http://example.com/formulario}}`

- Envia um pedido com um cabeçalho adicional, usando um método HTTP personalizado:

`curl --header {{'X-Meu-Cabecalho: 123'}} --request {{PUT}} {{http://example.com}}`

- Envia dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl --data {{'{"nome":"maria"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/usuarios/123}}`

- Passa ao pedido o nome de usuário e senha para autenticação no servidor:

`curl --user {{usuario}} {{http://example.com}}`

- Passa ao pedido o certificado do cliente e a chave para um recurso, omitindo a validação do certificado:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
