# lsof

> Lista arquivos abertos e os seus processos correspondentes.
> Nota: Privilégios de administrador (ou sudo) são necessários para listar arquivos abertos por outros.
> Mais informações: <https://manned.org/lsof>.

- Localizar os processos que têm um certo arquivo aberto:

`lsof {{caminho/para/arquivo}}`

- Localizar o processo que abriu uma porta de internet local:

`lsof -i :{{porta}}`

- Mostrar o ID (PID) do processo que abriu um arquivo especificado:

`lsof -t {{caminho/para/arquivo}}`

- Listar arquivos abertos por um certo usuário:

`lsof -u {{nome_usuario}}`

- Listar arquivos abertos por um certo comando ou processo:

`lsof -c {{nome_processo_ou_comando}}`

- Listar arquivos abertos por um certo processo, dado o seu PID:

`lsof -p {{PID}}`

- Listar arquivos abertos em um diretório:

`lsof +D {{caminho/para/diretório}}`

- Encontrar o processo que está ouvindo uma porta de TCP local:

`lsof -iTCP:{{porta}} -sTCP:LISTEN`
