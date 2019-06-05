# fcrackzip

> ZIP archive password cracking utility.

- Brute-force a password with a length of 4 to 8 characters, and contains only alphanumeric characters (order matters):

`fcrackzip -b -l 4-8 -c aA1 {{archive}}`

- Brute-force a password in verbose mode with a length of 3 characters that only contains lowercase characters, `$` and `%`:

`fcrackzip -v -b -l 3 -c a:$% {{archive}}`

- Bruteforce password with length 4 with only lowercase and special characters:

`fcrackzip -b -l 4 -c a! {{archive}}`

- Bruteforce password with length 5 with only digits starting from password "12345":

`fcrackzip -b -l 5 -c 1 -p 12345 {{archive}}`

- Crack password using a wordlist (verbose mode):

`fcrackzip -v -D -u -p {{wordlist}} {{archive}}`

- Benchmark cracking performance:

`fcrackzip -B`
