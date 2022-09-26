# base32

> Codifica ou decodifica um arquivo ou a entrada padrão (stdin) de/para Base32, para a saída padrão (stdout).
> Mais informações: <https://www.gnu.org/software/coreutils/base32>.

- Codifica um arquivo:

`base32 {{nome_do_arquivo}}`

- Decodifica um arquivo:

`base32 --decode {{nome_do_arquivo}}`

- Codifica a partir de stdin:

`{{algum_comando}} | base32`

- Decodifica a partir de stdin:

`{{algum_comando}} | base32 --decode`
