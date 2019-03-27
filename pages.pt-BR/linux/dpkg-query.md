# dpkg-query

> Ferramenta que mostra informações dos pacotes instalados.

- Exibe todos os pacotes instalados:

`dpkg-query -l`

- Exibe todos os pacotes instalados que correspondam ao critério de busca informado:

`dpkg-query -l '{{pattern}}'`

- List all files installed by a package:

`dpkg-query -L {{package_name}}`

- Show information about a package:

`dpkg-query -s {{package_name}}`
