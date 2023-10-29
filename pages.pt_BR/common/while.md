# while

> Loop simples da shell.
> Mais informações: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- Lê a entrada default (`stdin`) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do {{comando}}; sleep 1; done`
