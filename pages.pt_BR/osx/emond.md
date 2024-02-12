# emond

> Serviço Event Monitor que aceita eventos de vários serviços, os executa por meio de um mecanismo de regras simples, e executa ações.
> As ações podem executar comandos, enviar e-mails, ou mensagens SMS.
> Mais informações: <https://keith.github.io/xcode-man-pages/emond.8.html>.

- Inicia o daemon:

`emond`

- Especifica as regras para o emond processar, fornecendo um caminho para um arquivo ou diretório:

`emond -r {{caminho/para/arquivo_ou_diretório}}`

- Usa um arquivo de configuração específico:

`emond -c {{caminho/para/configuração}}`
