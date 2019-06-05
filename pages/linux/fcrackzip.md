# fcrackzip

> ZIP archive password cracking utility.

- Brute-force a password with a length of 4 to 8 characters, and contains only alphanumeric characters (order matters):

`fcrackzip --brute-force --length 4-8 --charset aA1 {{archive}}`

- Brute-force a password in verbose mode with a length of 3 characters that only contains lowercase characters, `$` and `%`:

`fcrackzip -v --brute-force --length 3 --charset a:$% {{archive}}`

- Brute-force a password that contains only lowercase and special characters:

`fcrackzip --brute-force --length 4 --charset a! {{archive}}`

- Brute-force a password containing only digits, starting from the password `12345`:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{archive}}`

- Crack a password using a wordlist:

`fcrackzip --use-unzip --dictionary --init-password {{wordlist}} {{archive}}`

- Benchmark cracking performance:

`fcrackzip --benchmark`
