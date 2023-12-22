# ssh-keyscan

> Obter as chaves públicas SSH de hosts remotos.
> Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obtém todas as chaves públicas SSH de um host remoto:

`ssh-keyscan {{host}}`

- Obtém todas as chaves públicas SSH de um host remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p {{porta}} {{host}}`

- Obtém determinados tipos de chaves públicas SSH de um host remoto:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- Atualiza manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado host:

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`
