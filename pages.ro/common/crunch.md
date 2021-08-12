# crunch

> Generator de liste de cuvinte.
> Mai multe informaţii: <https://sourceforge.net/projects/crunch-wordlist/>

- Ieșiți o listă de cuvinte de lungime de la 1 la 3 cu caractere mici:

`crunch {{1}} {{3}}`

- Ieșiți o listă de cuvinte hexazecimale de lungime 8:

`crunch {{8}} {{8}} {{0123456789abcdef}}`

- Ieșiți o listă a tuturor permutărilor de abc (lungimile nu sunt procesate):

`crunch {{1}} {{1}} -p {{abc}}`

- Ieșiți o listă a tuturor permutărilor șirurilor date (lungimile nu sunt procesate):

`crunch {{1}} {{1}} -p {{abc}} {{def}} {{ghi}}`

- Ieșiți o listă de cuvinte generate în funcție de modelul dat și un număr maxim de litere duplicate:

`crunch {{5}} {{5}} {{abcde123}} -t {{@@@12}} -d 2@`

- Scrieți o listă de cuvinte în fișiere bucăți de o anumită dimensiune, începând cu șirul dat:

`crunch {{3}} {{5}} -o {{START}} -b {{10kb}} -s {{abc}}`

- Scrieți o listă de cuvinte care se opresc cu șirul dat și inversând lista de cuvinte:

`crunch {{1}} {{5}} -o {{START}} -e {{abcde}} -i`

- Scrieți o listă de cuvinte în fișiere comprimate cu un număr specificat de cuvinte:

`crunch {{1}} {{5}} -o {{START}} -c {{1000}} -z {{gzip|bzip2|lzma|7z}}`
