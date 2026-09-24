# pssh

> Programa de SSH paralelo.
> Mais informações: <https://manned.org/pssh>.

- Executa um comando em dois servidores e imprime a saída em cada servidor em linha:

`pssh {{[-i|--inline]}} {{[-H|--host]}} "{{servidor1}} {{servidor2}}" {{hostname -i}}`

- Executa um comando e salva a saída em arquivos separados:

`pssh {{[-H|--host]}} {{servidor1}} {{[-H|--host]}} {{servidor2}} {{[-o|--outdir]}} {{caminho/para/diretório_de_saída}} {{hostname -i}}`

- Executa um comando em vários servidores, especificados em um arquivo separado por nova linha:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{caminho/para/arquivo_de_servidores}} {{hostname -i}}`

- Executa um comando como root (isso solicitará a senha do root):

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{caminho/para/arquivo_de_servidores}} {{[-A|--askpass]}} {{[-l|--user]}} {{nome_de_usuário_do_root}} {{hostname -i}}`

- Executa um comando com argumentos SSH adicionais:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{caminho/para/arquivo_de_servidores}} {{[-x|--extra-arg]}} "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- Executa um comando limitando o número de conexões paralelas para 10:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{caminho/para/arquivo_de_servidores}} {{[-p|-par]}} {{10}} '{{cd dir; ./script.sh; exit}}'`
