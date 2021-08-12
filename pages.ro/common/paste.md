# paste

> Îmbinare linii de fișiere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/paste>

- Alăturați-vă toate liniile într-o singură linie, folosind TAB ca delimitator:

`paste -s {{file}}`

- Alăturați-vă toate liniile într-o singură linie, folosind delimitatorul specificat:

`paste -s -d {{delimiter}} {{file}}`

- Mergeți două fișiere una lângă alta, fiecare în coloana sa, folosind TAB ca delimitator:

`paste {{file1}} {{file2}}`

- Mergeți două fișiere una lângă alta, fiecare în coloana sa, utilizând delimitatorul specificat:

`paste -d {{delimiter}} {{file1}} {{file2}}`

- Mergeți două fișiere, cu linii adăugate alternativ:

`paste -d '\n' {{file1}} {{file2}}`
