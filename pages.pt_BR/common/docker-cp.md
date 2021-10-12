# docker cp

> Copia arquivos ou diretórios entre filesystems do host e container.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/cp>.

- Copia um arquivo ou diretório de um host para um container:

`docker cp {{caminho/do/arquivo_ou_diretório_do_host}} {{nome_do_container}}:{{caminho/do/arquivo_ou_diretório_do_container}}`

- Copia um arquivo ou diretório de um container para o host:

`docker cp {{nome_do_container}}:{{caminho/do/arquivo_ou_diretório_do_container}} {{caminho/do/arquivo_ou_diretório_do_host}}`

- Copia um diretório de um host para um container, seguindo o link simbólico (copia os arquivos linkados diretamente e não o link simbólico):

`docker cp --follow-link {{caminho/do/arquivo_ou_diretório_linkado_do_host}} {{nome_do_container}}:{{caminho/do/arquivo_ou_diretório_do_container}}`
