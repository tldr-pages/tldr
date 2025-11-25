# apt-key

> Gerenciador de chaves utilizado pelo gerenciador de pacotes APT nas distribuições baseadas em Debian.
> Mais informações: <https://manned.org/apt-key.8>.

- Exibe as chaves confiáveis:

`apt-key list`

- Adiciona uma chave na lista de chaves confiáveis:

`apt-key add {{arquivo_da_chave_publica.asc}}`

- Remove uma chave da lista de chaves confiáveis:

`apt-key del {{key_id}}`

- Adiciona uma chave remota na lista de chaves confiáveis:

`wget {{[-qO|--quiet --output-document]}} - {{https://host.tld/arquivo.key}} | apt-key add -`

- Adiciona uma chave, de um servidor de chaves, na lista de chaves confiáveis:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
