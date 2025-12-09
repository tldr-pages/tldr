# ssh-add

> Gerencia as chaves SSH carregadas no ssh-agent.
> Certifique-se de que o ssh-agent esteja em execução para que as chaves sejam carregadas nele.
> Mais informações: <https://man.openbsd.org/ssh-add>.

- Adiciona as chaves SSH padrão em `~/.ssh` ao ssh-agent:

`ssh-add`

- Adiciona uma chave específica ao ssh-agent:

`ssh-add {{caminho/para/chave_privada}}`

- Lista as impressões digitais das chaves carregadas atualmente:

`ssh-add -l`

- Exclui uma chave do ssh-agent:

`ssh-add -d {{caminho/para/chave_privada}}`

- Exclui todas as chaves carregadas atualmente do ssh-agent:

`ssh-add -D`

- Adiciona uma chave ao ssh-agent e ao keychain:

`ssh-add -K {{caminho/para/chave_privada}}`
