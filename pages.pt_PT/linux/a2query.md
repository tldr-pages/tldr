# a2query

> Mostra configurações runtime do Apache em distribuições baseadas em Debian.
> Mais informações: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Lista módulos Apache activados:

`sudo a2query -m`

- Verifica de um módulo específico está instalado:

`sudo a2query -m {{module_name}}`

- Lista os hosts virtuais activados:

`sudo a2query -s`

- Mostra o módulo de multi processamento actualmente activado:

`sudo a2query -M`

- Mostra a versão do Apache:

`sudo a2query -v`
