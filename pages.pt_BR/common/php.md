# php

> Interface de linha de comando do PHP. Mais informações: <https://php.net>.

- Analisa e executa um script PHP:

`php {{caminho/para/arquivo}}`

- Verifica a sintaxe (lint) de um script PHP:

`php {{-l|--syntax-check}} {{caminho/para/arquivo}}`

- Executa o PHP de forma interativa:

`php {{-a|--interactive}}`

- Executa código PHP (não use as tags `<? ?>`; escape aspas duplas com barra invertida):

`php {{-r|--run}} "{{código}}"`

- Inicia o servidor web embutido do PHP no diretório atual:

`php {{-S|--server}} {{host}}:{{porta}}`

- Listar as extensões do PHP instaladas:

`php {{-m|--modules}}`

- Exibir informações sobre a configuração atual do PHP:

`php {{-i|--info}}`

- Exibir informações sobre uma função específica:

`php {{--rf|--rfunction}} {{nome_da_função}}`
