# tail

> Afișează ultima parte a unui fișier.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/tail>

- Afișează ultimele linii „num” din fișier:

`tail -n {{num}} {{file}}`

- Afișează toate fișierele de la linia „num”:

`tail -n +{{num}} {{file}}`

- Afișează ultimii octeți „num” în fișier:

`tail -c {{num}} {{file}}`

- Continuaţi să citiţi fişierul până la 'Ctrl + C':

`tail -f {{file}}`

- Continuați să citiți fișierul până la `Ctrl + C`, chiar dacă fișierul este rotit:

`tail -F {{file}}`

- Afișați ultimele linii „num” în „fișier” și reîmprospătați fiecare 'n' secunde:

`tail -n {{num}} -s {{n}} -f {{file}}`
