# git push

> Envia commits para um repositório remoto.
> Mais informações: <https://git-scm.com/docs/git-push>.

- Envia alterações locais na branch atual para sua contraparte remota padrão:

`git push`

- Envia alterações de uma branch local específica para sua contraparte remota:

`git push {{nome_remoto}} {{branch_local}}`

- Envia alterações de uma branch local específica para sua contraparte remota, e define a branch remota como o destino push/pull padrão da branch local:

`git push -u {{nome_remoto}} {{branch_local}}`

- Envia alterações de uma branch local específica para uma branch remota específica:

`git push {{nome_remoto}} {{branch_local}}:{{branch_remota}}`

- Envia alterações em todas as branches locais para suas contrapartes em um determinado repositório remoto:

`git push --all {{nome_remoto}}`

- Exclui uma branch em um repositório remoto:

`git push {{nome_remoto}} --delete {{branch_remota}}`

- Remove branches remotas que não tenham uma contraparte local:

`git push --prune {{nome_remoto}}`

- Publica etiquetas que ainda não estão no repositório remoto:

`git push --tags`
