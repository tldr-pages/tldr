# fcrackzip

> ZIP arhivă parola de cracare utilitate.
> Mai multe informaţii: <https://manned.org/fcrackzip>

- Forțați o parolă cu o lungime de 4 până la 8 caractere și conține numai caractere alfanumerice (chestiuni de ordine):

`fcrackzip --brute-force --length 4-8 --charset aA1 {{archive}}`

- Forțați o parolă în modul verbose cu o lungime de 3 caractere care conține doar caractere mici, `$` și `%`:

`fcrackzip -v --brute-force --length 3 --charset a:$% {{archive}}`

- Brute-vigoare o parolă care conține numai caractere mici și speciale:

`fcrackzip --brute-force --length 4 --charset a! {{archive}}`

- Brute-forțați o parolă care conține doar cifre, pornind de la parola `12345`:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{archive}}`

- Crack o parolă folosind o listă de cuvinte:

`fcrackzip --use-unzip --dictionary --init-password {{wordlist}} {{archive}}`

- Performanță de cracare de referință:

`fcrackzip --benchmark`
