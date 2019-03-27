# aspell

> Verificador de excrita interativo.

- Verifica a corretude de escrita um arquivo:

`aspell check {{path/to/file}}`

- Exibe as palavras escritas incorretamente no dispositivo de entrada padrão:

`cat {{file}} | aspell list`

- Exibe a lista de dicionários disponíveis:

`aspell dicts`

- Executa aspell utilizando um língua diferente (informe o código ISO 639 da língua):

`aspell --lang={{cs}}`

- Exibe as palavras escritas incorretamente no dispositivo de entrada padrão e ignora as palavras da lista pessoal:

`cat {{file}} | aspell --personal={{personal-word-list.pws}} {{list}}`
