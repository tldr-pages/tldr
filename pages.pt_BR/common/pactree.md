# img2pdf

> Ferramenta de conversão sem perdas de imagens para PDF.
> Mais informações: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- Converter múltiplas imagens para um único PDF, cada imagem sendo uma página:

`img2pdf {{caminho/da/imagem1.jpg}} {{caminho/da/imagem2.jpg}} --output {{caminho/do/arquivo.pdf}}`

- Converter para PDF apenas o primeiro quadro de uma imagem com múltiplos quadros:

`img2pdf {{caminho/do/arquivo.gif}} --first-frame-only --output {{caminho/do/arquivo.pdf}}`

- Auto-orientar a imagem, usar uma página A4 em modo paisagem e uma borda de 2cm horizontalmente e 5.1cm verticalmente:

`img2pdf {{caminho/do/arquivo.jpg}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{caminho/do/arquivo.pdf}}`

- Encolher apenas imagens maiores para um retângulo de 10cm por 15cm dentro de uma página de 30x20cm:

`img2pdf {{caminho/do/arquivo.tiff}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{caminho/do/arquivo.pdf}}`

- Converter uma imagem para PDF e especificar os metadados do arquivo resultante:

`img2pdf {{caminho/do/arquivo.png}} --title {{título}} --author {{autor}} --creationdate {{1970-01-31}} --keywords {{palavra_chave1 palavra_chave2}} --subject {{assunto}} --output {{caminho/do/arquivo.pdf}}`
