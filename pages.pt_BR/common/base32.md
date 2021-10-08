# base32

> Codifica ou decodifica um arquivo ou uma entrada padrão(stdin) de/para Base32, para uma saída padrão(stdout).
> Mais informações: <https://www.gnu.org/software/coreutils/base32>.

- Codifica o conteúdo de um arquivo para base32 e grava o resultado em stdout:

`base32 {{nome_arquivo}}`

- Decodifica o conteúdo de um arquivo em base32 e grava o resultado em stdout:

`base32 --decode {{nome_arquivo}}`

- Codifica a partir de stdin:

`{{algum_comando}} | base32`

- Decodifica a partir de stdin:
