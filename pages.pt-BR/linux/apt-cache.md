# apt-cache

> Buscador de pacotes para distribuições Debian e Ubuntu.

- Busca por pacotes, no cache de pacotes APT, que correspondam ao critério de busca informado:

`apt-cache search {{query}}`

- Exibe informações sobre um pacote:

`apt-cache show {{package}}`

- Exibe se um pacote está instalado e atualizado:

`apt-cache policy {{package}}`

- Exibe as dependências de um pacote:

`apt-cache depends {{package}}`

- Exibe pacotes que dependem de um pacote em particular:

`apt-cache rdepends {{package}}`
