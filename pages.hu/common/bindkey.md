# bindkey

> Billentyűkódok hozzáadása a Z-Shellhez. További információ: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- Egy gyorsbillentyű egy adott parancshoz való kötése:

`bindkey "{{^k}}" {{kill-line}}`

- A gyorsbillentyűzet egy adott billentyűsorozathoz kötése:

`bindkey -s '^o' 'cd ..\n'`

- Kulcstérképek megtekintése:

`bindkey -l`

- A gyorsbillentyű megtekintése egy billentyűtérképen:

`bindkey -M main`
