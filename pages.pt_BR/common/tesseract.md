# tesseract

> Motor de OCR (Reconhecimento Óptico de Caracteres).
> Mais informações: <https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc>.

- Reconhece o texto em uma imagem e salva-o no arquivo `saida.txt` (a extensão `.txt` é adicionada automaticamente):

`tesseract {{caminho/para/imagem.png}} {{saida}}`

- Especifica uma [l]inguagem personalizada (o padrão é inglês) com um código ISO 639-2 (ex. deu = Deutsch = Alemão):

`tesseract -l deu {{caminho/para/imagem.png}} {{caminho/para/saida}}`

- Lista os códigos de idiomas da ISO 639-2 instalados:

`tesseract --list-langs`

- Especifica um [m]odo de [s]egmentação de [p]ágina personalizado (o padrão é 3):

`tesseract --psm {{0..13}} {{caminho/para/imagem.png}} {{caminho/para/saida}}`

- Lista os modos de segmentação de página e suas descrições:

`tesseract --help-psm`
