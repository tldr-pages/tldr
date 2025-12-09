# ssh-keyscan

> Obter as chaves públicas SSH de servidores remotos.
> Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obtém todas as chaves públicas SSH de um servidor remoto:

`ssh-keyscan {{servidor}}`

- Obtém todas as chaves públicas SSH de um servidor remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p {{porta}} {{servidor}}`

- Obtém determinados tipos de chaves públicas SSH de um servidor remoto:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{servidor}}`

- Atualiza manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado servidor:

`ssh-keyscan -H {{servidor}} >> ~/.ssh/known_hosts`
