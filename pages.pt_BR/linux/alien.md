# alien

> Converter diferentes pacotes de instalação para outros formatos.
> Mais informações: <https://manned.org/alien>.

- Converte um arquivo de instalação específico para o formato Debian (extensão `.deb`):

`sudo alien --to-deb {{caminho/para/arquivo}}`

- Converte um arquivo de instalação específico para o formato Red Hat (extensão `.rpm`):

`sudo alien --to-rpm {{caminho/para/arquivo}}`

- Converte um arquivo de instalação específico para um arquivo de instalação do Slackware (extensão `.tgz`):

`sudo alien --to-tgz {{caminho/para/arquivo}}`

- Converte um arquivo de instalação específico para o formato Debian e instala no sistema:

`sudo alien --to-deb --install {{caminho/para/arquivo}}`
