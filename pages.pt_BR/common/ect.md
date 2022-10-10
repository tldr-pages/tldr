# ect

> Efficient Compression Tool.
> Otimizador de arquivos escrito em C++. Suporta arquivos do tipo `.png`, `.jpg`, `.gzip` and `.zip`.
> Mais informações: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Comprime um arquivo:

`ect {{caminho/para/arquivo.png}}`

- Comprime um arquivo com level de compressão específico e multithreading (1=Mais rápido (pior), 9=Mais lento (Melhor). O padrão é 3):

`ect -{{9}} --mt-deflate {{caminho/para/arquivo.zip}}`

- Comprime todos os arquivos em um diretório recursivamente:

`ect -recurse {{caminho/para/diretório}}`

- Comprime um arquivo, mantendo o tempo de modificação original:

`ect -keep {{caminho/para/arquivo.png}}`

- Comprime um arquivo, removendo metadados:

`ect -strip {{caminho/para/arquivo.png}}`
