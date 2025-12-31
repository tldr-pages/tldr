# history

> Histórico de linha da comando.
> Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- Exibe a lista de histórico de comandos com números de linha:

`history`

- Exibe os últimos 20 comandos (em Zsh ele exibe todos os comandos a partir do 20º):

`history {{20}}`

- Exibe histórico com data e hora em diferentes formatos (diponível apenas em Zsh):

`history -{{d|f|i|E}}`

- Limpa a lista do histórico de comandos (apenas para o shell Bash atual):

`history -c`

- Sobrescreve o arquivo de histórico com o histórico do shell Bash atual (frequentemente combinado com `history -c` para limpar o histórico):

`history -w`

- Deleta a entrada do histórico no deslocamento especificado:

`history -d {{deslocamento}}`
