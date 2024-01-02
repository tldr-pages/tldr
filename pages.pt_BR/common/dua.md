# dua

> Dua (Analisador de Uso de Disco) é uma ferramenta para análise conveniente do uso de disco dado um diretório.
> Mais informações: <https://github.com/Byron/dua-cli>.

- Analisa um diretório específico:

`dua {{caminho/para/diretorio}`

- Exibe o tamanho aparente ao invés do uso do disco:

`dua --apparent-size`

- Contabiliza arquivos hard-linked cada vez que eles são encontrados:

`dua --count-hard-links`

- Agrega o espaço em disco consumido de um ou mais diretórios ou arquivos:

`dua aggregate`

- Inicia a interface de usuário:

`dua interactive`

- Seleciona o formato para contagem de bytes:

`dua --format {{metric|binary|bytes|GB|GiB|MB|MiB}}`

- Escolhe o número de threads a serem usadas:

`dua --threads {{numero}}`
