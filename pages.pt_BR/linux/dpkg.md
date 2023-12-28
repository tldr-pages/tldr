# dpkg

> Gerenciador de pacotes Debian.
> Alguns subcomandos como `dpkg deb` tem sua própia documentação de uso.
> Mais informações: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Instala um pacote:

`dpkg -i {{arquivo.deb}}`

- Remove um pacote:

`dpkg -r {{nome_do_pacote}}`

- Exibe os pacotes correspondentes ao critério de busca:

`dpkg -l {{criterio_de_busca}}`

- Exibe o conteúdo do pacote:

`dpkg -L {{nome_do_pacote}}`

- Exibe o conteúdo do arquivo de um pacote:

`dpkg -c {{arquivo.deb}}`

- Apresenta o pacote proprietário de um determinado arquivo:

`dpkg -S {{nome_do_arquivo}}`
