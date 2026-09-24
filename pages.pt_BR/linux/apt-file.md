# apt-file

> Busca arquivos nos pacotes APT, incluindo os não instalados.
> Mais informações: <https://manned.org/apt-file>.

- Atualiza as informações dos pacotes:

`sudo apt update`

- Busca por pacotes que contêm o arquivo ou caminho especificado:

`apt-file {{[find|search]}} {{caminho_parcial/para/arquivo}}`

- Lista o conteúdo de um pacote específico:

`apt-file list {{nome_do_pacote}}`

- Busca pacotes que correspondem à expressão regular:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{expressao_regular}}`
