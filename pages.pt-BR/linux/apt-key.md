# apt-key

> Gerenciador de chaves utilizado pelo gerenciador de pacotes APT nas distribuições baseadas em Debian.

- Exibir as chaves confiáveis:

`apt-key list`

- Adicionar uma chave na lista de chaves confiáveis:

`apt-key add {{arquivo_da_chave_publica.asc}}`

- Remover uma chave da lista de chaves confiáveis:

`apt-key del {{key_id}}`

- Adicionar uma chave remota na lista de chaves confiáveis:

`wget -qO - {{https://host.tld/arquivo.key}} | apt-key add -`

- Adicionar uma chave, de um servidor de chaves, na lista de chaves confiáveis:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
