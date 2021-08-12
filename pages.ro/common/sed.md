# sed

> Editați textul într-un mod scriptabil.
> Mai multe informaţii: <https://man.archlinux.org/man/sed.1>

- Înlocuiți prima apariție a unei expresii regulate în fiecare linie a unui fișier și imprimați rezultatul:

`sed 's/{{regular_expression}}/{{replace}}/' {{filename}}`

- Înlocuiți toate aparițiile unei expresii regulate extinse într-un fișier și imprimați rezultatul:

`sed -r 's/{{regular_expression}}/{{replace}}/g' {{filename}}`

- Înlocuiți toate aparițiile unui șir într-un fișier, suprascriind fișierul (adică în loc):

`sed -i 's/{{find}}/{{replace}}/g' {{filename}}`

- Înlocuiți numai pe liniile care corespund modelului liniei:

`sed '/{{line_pattern}}/s/{{find}}/{{replace}}/' {{filename}}`

- Ștergeți liniile care se potrivesc modelului liniei:

`sed '/{{line_pattern}}/d' {{filename}}`

- Imprimați primele 11 linii ale unui fișier:

`sed 11q {{filename}}`

- Aplicați mai multe expresii de găsire-înlocuire la un fișier:

`sed -e 's/{{find}}/{{replace}}/' -e 's/{{find}}/{{replace}}/' {{filename}}`

- Înlocuiți separatorul `/` cu orice alt caracter care nu este utilizat în găsirea sau înlocuirea modelelor, de exemplu, `#`:

`sed 's#{{find}}#{{replace}}#' {{filename}}`
