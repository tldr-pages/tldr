# magick convert

> Converte formatos de imagem, escala, adiciona, e cria imagens, e muito mais.
> Nota: Essa ferramenta (previamente conhecida como `convert`) foi substituída por `magick` no ImageMagick 7+.
> Mais informações: <https://imagemagick.org/script/convert.php>.

- Converte uma imagem do formato JPEG para o formato PNG:

`magick convert {{caminho/para/imagem_de_entrada.jpg}} {{caminho/para/imagem_de_saida.png}}`

- Escala uma imagem para 50% do seu tamanho original:

`magick convert {{caminho/para/imagem_de_entrada.png}} -resize 50% {{caminho/para/imagem_de_saida.png}}`

- Escala uma imagem, mantendo as suas proporções originais, para uma dimensão máxima de 640x480:

`magick convert {{caminho/para/imagem_de_entrada.png}} -resize 640x480 {{caminho/para/imagem_de_saida.png}}`

- Escala uma imagem para ter oum tamanho de arquivo específico:

`magick convert {{caminho/para/imagem_de_entrada.png}} -define jpeg:extent=512kb {{caminho/para/imagem_de_saida.jpg}}`

- Junta imagens verticalmente/horizontalmente e deixa o espaço vazio transparente:

`magick convert -background none {{caminho/para/imagem1.png caminho/para/imagem2.png ...}} {{-append|+append}} {{caminho/para/imagem_de_saida.png}}`

- Cria um GIF a partir de uma série de imagens, com um intervalo de 100ms entre elas:

`magick convert {{caminho/para/imagem1.png caminho/para/imagem2.png ...}} -delay {{10}} {{caminho/para/animacao.gif}}`

- Cria uma imagem apenas com um fundo sólido vermelho:

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{caminho/para/imagem.png}}`

- Cria um favicon de várias imagens de tamanhos diferentes:

`magick convert {{caminho/para/imagem1.png caminho/para/imagem2.png ...}} {{caminho/para/favicon.ico}}`
