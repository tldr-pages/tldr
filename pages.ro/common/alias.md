# alias

> Creează aliasuri — cuvinte care sunt înlocuite cu un șir de comandă.
> Aliasurile expiră cu sesiunea de shell curentă, dacă nu sunt definite în fișierul de configurare al shell-ului, de exemplu `~/.bashrc`.
> Mai multe informaţii: <https://tldp.org/LDP/abs/html/aliases.html>

- Listează toate pseudonimele:

`alias`

- Creați un alias generic:

`alias {{word}}="{{command}}"`

- Vizualizați comanda asociată unui alias dat:

`alias {{word}}`

- Eliminați o comandă aliasată:

`unalias {{word}}`

- Transformați `rm` într-o comandă interactivă:

`alias {{rm}}="{{rm -i}}"`

- Creați `la` ca o scurtătură pentru `ls -a`:

`alias {{la}}="{{ls -a}}"`
