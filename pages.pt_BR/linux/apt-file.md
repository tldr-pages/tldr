# apt-file

> Buscador de arquivos nos pacotes apt, incluindo os não instalados.
> Mais informações: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Atualiza as informações dos pacotes a partir de todos os repositórios remotos:

`sudo apt update`

- Busca por pacotes que contêm o arquivo ou caminho especificado:

`apt-file search {{nome_do_pacote_ou_caminho}}`

- Lista o conteúdo de um pacote específico:

`apt-file list {{nome_do_pacote}}`
