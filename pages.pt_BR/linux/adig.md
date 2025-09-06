# adig

> Imprime informações recebidas dos servidores do Sistema de Domínio de Nome(DNS).
> Mais informações: <https://manned.org/adig>.

- Exibe uma gravação A (padrão) do DNS por nome(s) de servidor(es):

`adig {{examplo.com}}`

- Exibe uma saída de [d]epuração extra:

`adig -d {{examplo.com}}`

- Conecte-se a um servidor DNS específico:

`adig -s {{1.2.3.4}} {{examplo.com}}`

- Use uma porta TCP específica para se conectar ao servidor DNS:

`adig -T {{port}} {{examplo.com}}`

- Use uma porta UDP específica para se conectar ao servidor DNS:

`adig -U {{port}} {{examplo.com}}`
