# chown

> Muda o usuário e grupo donos de arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Muda o usuário que é dono de um arquivo ou diretório:

`chown {{usuario}} {{caminho/para/arquivo_ou_diretório}}`

- Muda o usuário e grupo que são donos de um arquivo/diretório:

`chown {{usuario}}:{{grupo}} {{caminho/para/arquivo_ou_diretório}}`

- Muda o usuário dono e o grupo para que ambos tenha o nome `usuario`:

`chown {{usuario}}: {{caminho/para/arquivo_ou_diretorio}}`

- Recursivamente muda o dono de um diretório e seu conteúdo:

`chown {{[-R|--recursive]}} {{usuario}} {{caminho/para/diretório}}`

- Muda o dono de um link simbólico:

`chown {{[-h|--no-dereference]}} {{usuario}} {{caminho/para/symlink}}`

- Muda o dono de um arquivo/diretório para ficar igual a um arquivo de referência:

`chown --reference {{caminho/para/arquivo_de_referência}} {{caminho/para/arquivo_ou_diretório}}`
