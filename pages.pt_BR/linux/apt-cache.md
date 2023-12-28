# apt-cache

> Buscador de pacotes para distribuições baseadas no Debian.
> Mais informações: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Busca pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search {{criterio_de_busca}}`

- Exibe informações sobre um pacote:

`apt-cache show {{nome_do_pacote}}`

- Informa a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy {{nome_do_pacote}}`

- Exibe as dependências de um pacote:

`apt-cache depends {{nome_do_pacote}}`

- Exibe pacotes dependentes de um determinado pacote:

`apt-cache rdepends {{nome_do_pacote}}`
