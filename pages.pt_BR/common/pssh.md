# pssh

> Programa de SSH paralelo.
> Mais informações: <https://manned.org/pssh>.

- Executa um comando em dois servidores e imprime a saída em cada servidor em linha:

`pssh -i -H "{{servidor1}} {{servidor2}}" {{hostname -i}}`

- Executa um comando e salva a saída em arquivos separados:

`pssh -H {{servidor1}} -H {{servidor2}} -o {{caminho/para/diretório_de_saída}} {{hostname -i}}`

- Executa um comando em vários servidores, especificados em um arquivo separado por nova linha:

`pssh -i -h {{caminho/para/arquivo_de_servidores}} {{hostname -i}}`

- Executa um comando como root (isso solicitará a senha do root):

`pssh -i -h {{caminho/para/arquivo_de_servidores}} -A -l {{nome_de_usuário_do_root}} {{hostname -i}}`

- Executa um comando com argumentos SSH adicionais:

`pssh -i -h {{caminho/para/arquivo_de_servidores}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- Executa um comando limitando o número de conexões paralelas para 10:

`pssh -i -h {{caminho/para/arquivo_de_servidores}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
