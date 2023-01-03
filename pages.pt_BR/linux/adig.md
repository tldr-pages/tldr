# adig

> Imprime informações recebidas dos servidores do Sistema de Domínio de Nome(DNS).
> Mais informações: <https://manned.org/adig>.

- Exibe uma gravação A (padrão) do DNS por nome(s) de servidor(es):

`adig {{examplo.com}}`

- Exibe uma saída de [d]epuração extra:

`adig -d {{examplo.com}}`

- Conecta ao servidor DNS [e]specificado:

`adig -s {{1.2.3.4}} {{examplo.com}}`

- Usa porta TCP específica para conectar ao servidor DNS:

`adig -T {{port}} {{examplo.com}}`

- Use uma porta UDP específica para se conectar ao servidor DNS:

`adig -U {{port}} {{examplo.com}}`
