# base64

> Codifica ou decodifica um arquivo ou uma entrada padrão (stdin) de/para Base64, para uma saída padrão (stdout).
> Mais informações: <https://www.gnu.org/software/coreutils/base64>.

- Codifica o conteúdo de um arquivo para base64 e grava o resultado em stdout:

`base64 {{nome_arquivo}}`

- Decodifica o conteúdo de um arquivo em base64 e grava o resultado em stdout:

`base64 --decode {{nome_arquivo}}`

- Codifica a partir de stdin:

`{{algum_comando}} | base64`

- Decodifica a partir de stdin:

`{{algum_comando}} | base64 --decode`
