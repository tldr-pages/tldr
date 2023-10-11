# ssh-copy-id

> Instala a sua chave pública no arquivo authorized_keys de uma máquina remota.
> Mais informações: <https://manned.org/ssh-copy-id>.

- Copiar suas chaves para a máquina remota:

`ssh-copy-id {{nome_de_usuário@host_remoto}}`

- Copiar a chave pública fornecida para o remoto:

`ssh-copy-id -i {{caminho/para/certificado}} {{nome_de_usuário}}@{{host_remoto}}`

- Copiar a chave pública fornecida para o remoto usando uma porta específica:

`ssh-copy-id -i {{caminho/para/certificado}} -p {{porta}} {{nome_de_usuário}}@{{host_remoto}}`
