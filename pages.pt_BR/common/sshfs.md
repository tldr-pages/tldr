# sshfs

> Cliente de sistema de arquivos baseado em SSH.
> Mais informações: <https://github.com/libfuse/sshfs>.

- Monta um diretório remoto:

`sshfs {{nome_do_usuário}}@{{host_remoto}}:{{diretório_remoto}} {{ponto_de_montagem}}`

- Desmonta um diretório remoto:

`umount {{ponto_de_montagem}}`

- Monta um diretório remoto de um servidor com uma porta específica:

`sshfs {{nome_do_usuário}}@{{host_remoto}}:{{diretório_remoto}} -p {{2222}}`

- Usa compressão:

`sshfs {{nome_do_usuário}}@{{host_remoto}}:{{diretório_remoto}} -C`

- Segue links simbólicos:

`sshfs -o follow_symlinks {{nome_do_usuário}}@{{host_remoto}}:{{diretório_remoto}} {{ponto_de_montagem}}`
