# apt-key

> Gerenciador de chaves utilizado pelo gerenciador de pacotes APT nas distribuições Debian e Ubuntu.

- Exibe as chaves confiáveis:

`apt-key list`

- Adiciona uma chave a lista de chaves confiáveis:

`apt-key add {{public_key_file.asc}}`

- Remove uma chave a lista de chaves confiáveis:

`apt-key del {{key_id}}`

- Adiciona uma chave remota a lista de chaves confiáveis:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Adiciona uma chave, de um servidor de chaves, a lista de chaves confiáveis:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
