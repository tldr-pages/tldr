# dpkg

> Gerenciador de pacotes Debian.
> Alguns subcomandos como `dpkg deb` tem sua própia documentação de uso.
> Mais informações: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Instalar um pacote:

`dpkg -i {{arquivo.deb}}`

- Remover um pacote:

`dpkg -r {{nome_do_pacote}}`

- Exibir os pacotes correspondentes ao critério de busca:

`dpkg -l {{criterio_de_busca}}`

- Exibe o conteúdo do pacote:

`dpkg -L {{nome_do_pacote}}`

- Exibir o conteúdo do arquivo de um pacote:

`dpkg -c {{arquivo.deb}}`

- Apresentar o pacote proprietário de um determinado arquivo:

`dpkg -S {{nome_do_arquivo}}`
