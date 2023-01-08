# pip install

> Instala pacotes Python.
> Mais informações: <https://pip.pypa.io>.

- Instala um pacote:

`pip install {{nome_pacote}}`

- Instala uma versão específica de um pacote:

`pip install {{nome_pacote}}=={{versão_do_pacote}}`

- Instala pacotes listados em um arquivo:

`pip install --requirement {{requirements.txt}}`

- Instala pacotes a partir de uma URL ou arquivo local (.tar.gz | .whl):

`pip install --find-links {{url|caminho/do/arquivo}}`

- Instala o pacote local no diretório atual no modo de desenvolvimento (editável):

`pip install --editable {{.}}`
