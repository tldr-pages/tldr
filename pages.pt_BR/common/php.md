# php

> Interface de linha de comando do PHP. Mais informações: <https://php.net>.

- Analisar e executar um script PHP:

`php {{caminho/para/arquivo}}`

- Verificar a sintaxe (lint) de um script PHP:

`php -l {{caminho/para/arquivo}}`

- Executar o PHP de forma interativa:

`php -a`

- Executar código PHP (não use as tags `<? ?>`; escape aspas duplas com barra invertida):

`php -r "{{código}}"`

- Iniciar o servidor web embutido do PHP no diretório atual:

`php -S {{host}}:{{porta}}`

- Listar as extensões do PHP instaladas:

`php -m`

- Exibir informações sobre a configuração atual do PHP:

`php -i`

- Exibir informações sobre uma função específica:

`php --rf {{nome_da_função}}`
