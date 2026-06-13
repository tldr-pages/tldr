# ssh-copy-id

> Instala a sua chave pública no arquivo authorized_keys de uma máquina remota.
> Mais informações: <https://manned.org/ssh-copy-id>.

- Copia suas chaves para a máquina remota:

`ssh-copy-id {{nome_de_usuário}}@{{máquina_remota}}`

- Copia a chave pública fornecida para a máquina remota:

`ssh-copy-id -i {{caminho/para/certificado}} {{nome_de_usuário}}@{{maquina_remota}}`

- Copia a chave pública fornecida para a máquina remota usando uma porta específica:

`ssh-copy-id -i {{caminho/para/certificado}} -p {{porta}} {{nome_de_usuário}}@{{maquina_remota}}`
