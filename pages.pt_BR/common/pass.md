# pass

> Guarda e lê senhas ou outras informações sensíveis.
> Todos os dados são criptografados com GPG e gerenciados por um repositório Git.
> Mais informações: <https://www.passwordstore.org>.

- Inicia (ou recriptografa) o armazenamento usando um ou mais IDs GPG:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Salva uma nova senha e informações adicionais (pressione `<Ctrl d>` em uma nova linha para completar):

`pass insert {{[-m|--multiline]}} {{caminho/para/arquivo}}`

- Edita uma entrada:

`pass edit {{caminho/para/dados}}`

- Copia uma senha (Primeira linha do arquivo de dados) para a área de transferência:

`pass {{[-c|--clip]}} {{caminho/para/dados}}`

- Lista toda a árvore de armazenamento:

`pass`

- Gera uma nova senha aleatória com um comprimento (num) específico e copia para a área de transferência:

`pass generate {{[-c|--clip]}} {{caminho/para/dados}} {{num}}`

- Inicializa um novo repositório Git (todas as mudanças feitas pelo pass são commitadas automaticamente):

`pass git init`

- Executa um comando Git no repositório de senhas:

`pass git {{comando}}`
