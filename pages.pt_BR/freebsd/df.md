# df

> Exibe uma visão geral do uso de espaço de disco do sistema de arquivos.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?df>.

- Exibe todos os sistemas de arquivos e seu uso de disco usando unidades 512-bytes:

`df`

- Usa unidades legíveis para [h]umanos (baseadas em potências de 1024) e exibe um total:

`df -h -c`

- Usa unidades legíveis para [h]umanos (baseadas em potências de 1000):

`df -{{-si|H}}`

- Exibe o sistema de arquivos e seu uso do disco contendo o arquivo ou diretório dado:

`df {{caminho/para/arquivo_ou_diretório}}`

- Inclui estatísticas do número de nós livres e usados incluindo [T]ipos do sistema de arquivos:

`df -iT`

- Usa unidades 1024-bytes ao escrever figuras de espaço:

`df -k`

- Exibe informação em uma maneira [p]ortátil:

`df -P`
