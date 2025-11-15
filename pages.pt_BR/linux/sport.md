# sport

> Busque e instale Slackbuilds.
> Mais informações: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- Puxa a lista de SlackBuilds para rodar `sport` pela primeira vez:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- Puxa qualquer atualização para a árvore do sistema via `rsync`:

`sudo sport rsync`

- Procura um pacote pelo nome:

`sport search "{{palavra_chave}}"`

- Checa se um pacote está instalado:

`sport check {{pacote}}`

- Exibe os arquivos README e `.info` de um pacote:

`sport cat {{pacote}}`

- Instala um pacote uma vez que as dependências estejam instaladas:

`sudo sport install {{pacote}}`

- Instala uma lista de pacotes de um arquivo (formato: pacotes separados por espaço):

`sudo sport install $(< {{caminho/para/lista}})`
