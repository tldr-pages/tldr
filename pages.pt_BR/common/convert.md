# convert

> Ferramenta de conversão de imagens da ImageMagick.
> Mais informações: <https://imagemagick.org/script/convert.php>.

- Converte uma imagem do formato JPG para o formato PNG:

`convert {{imagem.jpg}} {{imagem.png}}`

- Escala uma imagem para 50% do seu tamanho original:

`convert {{imagem.png}} -resize 50% {{nova_imagem.png}}`

- Escala uma imagem, mantendo as suas proporções originais, para uma dimensão máxima de 640x480:

`convert {{imagem.png}} -resize 640x480 {{nova_imagem.png}}`

- Junta várias imagens horizontalmente:

`convert {{imagem1.png}} {{imagem2.png}} {{imagem3.png}} +append {{nova_imagem.png}}`

- Cria um GIF a partir de uma série de imagens, com um intervalo de 100ms entre elas:

`convert {{imagem1.png}} {{imagem2.png}} {{imagem3.png}} -delay {{100}} {{nova_imagem.gif}}`

- Cria uma nova imagem de tamanho 800x600 com apenas um fundo sólido vermelho:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{imagem.png}}`
