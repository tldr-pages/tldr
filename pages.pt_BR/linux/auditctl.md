# auditctl

> Utilitário para controlar o comportamento, obter o status e gerenciar regras do Sistema de Auditoria do Linux.
> Mais informações: <https://manned.org/auditctl>.

- Exibe o e[s]tatus do sistema de auditoria:

`sudo auditctl -s`

- [l]ista todas as regras de auditoria atualmente carregadas:

`sudo auditctl -l`

- [D]eleta todas as regras de auditoria:

`sudo auditctl -D`

- Habilita ou desabilita o sistema de auditoria:

`sudo auditctl -e {{1|0}}`

- Monitora um arquivo em busca de alterações:

`sudo auditctl -a always,exit -F arch=b64 -F path=/{{caminho/para/arquivo}} -F perm=wa`

- Monitora recursivamente um diretório em busca de alterações:

`sudo auditctl -a always,exit -F arch=b64 -F dir=/{{caminho/para/diretorio}}/ -F perm=wa`

- Mostra ajuda:

`auditctl -h`
