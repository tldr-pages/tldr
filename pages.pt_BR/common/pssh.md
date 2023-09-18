# pssh

> Programa de SSH paralelo.
> Mais informações: <https://manned.org/pssh>.

- Executar um comando em dois hosts e imprimir a saída em cada servidor em linha:

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- Executar um comando e salvar a saída em arquivos separados:

`pssh -H {{host1}} -H {{host2}} -o {{caminho/para/diretório_de_saída}} {{hostname -i}}`

- Executar um comando em vários hosts, especificados em um arquivo separado por nova linha:

`pssh -i -h {{caminho/para/arquivo_de_hosts}} {{hostname -i}}`

- Executar um comando como root (isso solicitará a senha do root):

`pssh -i -h {{caminho/para/arquivo_de_hosts}} -A -l {{nome_de_usuário_do_root}} {{hostname -i}}`

- Executar um comando com argumentos SSH adicionais:

`pssh -i -h {{caminho/para/arquivo_de_hosts}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- Executar um comando limitando o número de conexões paralelas para 10:

`pssh -i -h {{caminho/para/arquivo_de_hosts}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
