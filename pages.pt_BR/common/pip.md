# pip

> Gerenciador de pacotes para Python.
> Alguns sub-comandos, como `pip install` possuem sua própria documentação.
> Mais informações: <https://pip.pypa.io>.

- Instala um pacote (veja `pip install` para mais exemplos de instalação):

`pip install {{nome_pacote}}`

- Instala um pacote no diretório do usuário em vez do local padrão do sistema:

`pip install --user {{nome_pacote}}`

- Atualiza um pacote:

`pip install --upgrade {{nome_pacote}}`

- Desinstala um pacote:

`pip uninstall {{nome_pacote}}`

- Salva os pacotes instalados em um arquivo:

`pip freeze > {{requirements.txt}}`

- Mostra informações sobre um pacote instalado:

`pip show {{nome_pacote}}`

- Instala pacotes a partir de um arquivo:

`pip install --requirement {{requirements.txt}}`
