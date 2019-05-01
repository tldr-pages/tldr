# apt-cache

> Buscador de pacotes para distribuições baseadas no Debian.

- Buscar pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search {{criterio_de_busca}}`

- Exibir informações sobre um pacote:

`apt-cache show {{nome_do_pacote}}`

- Informar a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy {{nome_do_pacote}}`

- Exibir as dependências de um pacote:

`apt-cache depends {{nome_do_pacote}}`

- Exibir pacotes dependentes de um determinado pacote:

`apt-cache rdepends {{nome_do_pacote}}`
