# watchexec

> Executați comenzi arbitrare atunci când fișierele se modifică.
> Mai multe informaţii: <https://github.com/watchexec/watchexec>

- Apelați `ls -la` atunci când orice fișier din directorul curent se schimbă:

`watchexec -- {{ls -la}}`

- Rulați `make` atunci când orice fișiere JavaScript, CSS și HTML din directorul curent se schimbă:

`watchexec --exts {{js,css,html}} make`

- Rulați `make` atunci când orice fișier din subdirectoarele `lib` sau `src` se modifică:

`watchexec --watch {{lib}} --watch {{src}} {{make}}`

- Apelați/reporniți `my_server` atunci când orice fișier din directorul curent se schimbă, trimițând `SIGKILL` pentru a opri procesul de copil:

`watchexec --restart --signal {{SIGKILL}} {{my_server}}`
