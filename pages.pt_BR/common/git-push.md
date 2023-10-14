# git push

> Envia commits para um repositório remoto.
> Mais informações: <https://git-scm.com/docs/git-push>.

- Envia alterações locais na ramificação atual para sua contraparte remota padrão:

`git push`

- Envia alterações de uma ramificação local específica para sua contraparte remota:

`git push {{nome_remoto}} {{ramificação_local}}`

- Envia alterações de uma ramificação local específica para sua contraparte remota, e define a ramificação remota como o destino push/pull padrão da ramificação local:

`git push -u {{nome_remoto}} {{ramificação_local}}`

- Envia alterações de uma ramificação local específica para uma ramificação remota específica:

`git push {{nome_remoto}} {{ramificação_local}}:{{ramificação_remota}}`

- Envia alterações em todas as ramificações locais para suas contrapartes em um determinado repositório remoto:

`git push --all {{nome_remoto}}`

- Exclui uma ramificação em um repositório remoto:

`git push {{nome_remoto}} --delete {{ramificação_remota}}`

- Remove ramificações remotas que não tenham uma contraparte local:

`git push --prune {{nome_remoto}}`

- Publica etiquetas que ainda não estão no repositório remoto:

`git push --tags`
