# a2query

> Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian.
> Mais informações: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Lista módulos ativos do Apache:

`sudo a2query -m`

- Verifica se um módulo específico está instalado:

`sudo a2query -m {{nome_do_modulo}}`

- Lista host virtuais ativos:

`sudo a2query -s`

- Exibe o módulo de multi processamento atualmente ativo:

`sudo a2query -M`

- Mostra a versão do Apache:

`sudo a2query -v`
