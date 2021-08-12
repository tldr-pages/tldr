# strings

> Găsiți șiruri de caractere imprimabile într-un fișier obiect sau binar.

- Imprimați toate șirurile într-un binar:

`strings {{file}}`

- Limitați rezultatele la șiruri de cel puțin *lungime* caractere lungi:

`strings -n {{length}} {{file}}`

- Prefixează fiecare rezultat cu decalajul său în fișier:

`strings -t d {{file}}`

- Prefixează fiecare rezultat cu decalajul său în fișier în hexazecimal:

`strings -t x {{file}}`
