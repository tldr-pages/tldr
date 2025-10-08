# tesseract

> Mecanismo OCR (Reconhecimento Óptico de Caracteres).
> Mais Informações: <https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc>.

- Reconhece o texto em uma imagem e salva-o no arquivo `saida.txt` (a extensão `.txt` é adicionada automaticamente):

`tesseract {{imagem.png}} {{saida}}`

- Especifica um outro idioma (do padrão é inglês) com um código ISO 639-2 (e.g. por = Português):

`tesseract -l por {{imagem.png}} {{saida}}`

- Lista os códigos de idiomas disponíveis na ISO 639-2

`tesseract --list-langs`

- Especifica um modo de segmentação de página personalizado (o padrão é 3):

`tesseract --psm {{0_to_10}} {{imagem.png}} {{saida}}`

- Lista os modos de segmentação de páginas de lista e suas descrições:

`tesseract --help-psm`
