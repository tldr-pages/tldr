# ssh-keyscan

> Obter as chaves públicas SSH de hosts remotos.
> Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obter todas as chaves públicas SSH de um host remoto:

`ssh-keyscan {{host}}`

- Obter todas as chaves públicas SSH de um host remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p {{porta}} {{host}}`

- Obter determinados tipos de chaves públicas SSH de um host remoto:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- Atualizar manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado host:

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`
