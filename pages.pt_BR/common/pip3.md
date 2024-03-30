# pip3

> Gerenciador de pacotes Python.
> Mais informações: <https://pip.pypa.io>.

- Instala um pacote:

`pip3 install {{nome_pacote}}`

- Instala uma versão específica de um pacote:

`pip3 install {{nome_pacote}}=={{versão_pacote}}`

- Atualiza um pacote:

`pip3 install --upgrade {{nome_pacote}}`

- Desinstala um pacote:

`pip3 uninstall {{nome_pacote}}`

- Salva a lista de pacotes instalados em um arquivo:

`pip3 freeze > {{requirements.txt}}`

- Instala pacotes salvos em um arquivo:

`pip3 install --requirement {{requirements.txt}}`

- Mostra informações sobre um pacote instalado:

`pip3 show {{nome_pacote}}`
