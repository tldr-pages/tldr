# a2query

> Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian.
> Mais informações: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Listar módulos ativos do Apache:

`sudo a2query -m`

- Verificar se um módulo específico está instalado:

`sudo a2query -m {{nome_do_modulo}}`

- Listar host virtuais ativos:

`sudo a2query -s`

- Exibir o módulo de multi processamento atualmente ativo:

`sudo a2query -M`

- Mostrar a versão do Apache:

`sudo a2query -v`
