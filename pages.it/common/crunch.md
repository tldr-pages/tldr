# crunch

> Generatore di wordlist.
> Maggiori informazioni: <https://manned.org/crunch>.

- Genera una lista di parole di lunghezza da 1 a 3 con solo caratteri minuscoli:

`crunch {{1}} {{3}}`

- Genera una lista di parole esadecimali di lunghezza 8:

`crunch {{8}} {{8}} {{0123456789abcdef}}`

- Genera una lista con tutte le permutazioni di "abc" (le lunghezze non vengono elaborate):

`crunch {{1}} {{1}} -p {{abc}}`

- Genera una lista con tutte le permutazioni delle stringhe fornite (le lunghezze non vengono elaborate):

`crunch {{1}} {{1}} -p {{abc}} {{def}} {{ghi}}`

- Genera una lista di parole secondo un modello specifico e un numero massimo di lettere duplicate:

`crunch {{5}} {{5}} {{abcde123}} -t {{@@@12}} -d 2@`

- Scrive una lista di parole in file suddivisi per dimensione, iniziando con una stringa specificata:

`crunch {{3}} {{5}} -o {{START}} -b {{10kb}} -s {{abc}}`

- Scrive una lista di parole terminando con una stringa specificata e invertendo la wordlist:

`crunch {{1}} {{5}} -o {{START}} -e {{abcde}} -i`

- Scrive una lista di parole in file compressi suddivisi per numero di parole:

`crunch {{1}} {{5}} -o {{START}} -c {{1000}} -z {{gzip|bzip2|lzma|7z}}`
