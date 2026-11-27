# apt-cache

> Buscador de pacotes para distribuições baseadas no Debian.
> Mais informações: <https://manned.org/apt-cache>.

- Busca pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search {{criterio_de_busca}}`

- Exibe informações sobre um pacote:

`apt-cache show {{pacote}}`

- Informa a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy {{pacote}}`

- Exibe as dependências de um pacote:

`apt-cache depends {{pacote}}`

- Exibe pacotes dependentes de um determinado pacote:

`apt-cache rdepends {{pacote}}`
