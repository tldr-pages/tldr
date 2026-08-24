# asciiart

> Converte imagens para ASCII.
> Mais informações: <https://github.com/nodanaonlyzuul/asciiart#in-the-command-line>.

- Lê uma imagem de um arquivo e imprime em ASCII:

`asciiart {{caminho/para/imagem.jpg}}`

- Lê uma imagem de uma URL e imprime em ASCII:

`asciiart {{www.example.com/imagem.jpg}}`

- Escolha a largura da saída (o padrão é 100):

`asciiart {{[-w|--width]}} {{50}} {{caminho/para/imagem.jpg}}`

- Imprime com cor:

`asciiart {{[-c|--color]}} {{caminho/para/imagem.jpg}}`

- Escolha o formato de saída (o padrão é text):

`asciiart {{[-f|--format]}} {{text|html}} {{caminho/para/imagem.jpg}}`

- Inverte o mapeamento dos caracteres:

`asciiart {{[-i|--invert-chars]}} {{caminho/para/imagem.jpg}}`
