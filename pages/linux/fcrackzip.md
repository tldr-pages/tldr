# fcrackzip

> ZIP archive password cracking utility.
> More information: <https://manned.org/fcrackzip>.

- Brute-force a password with a length of 4 to 8 characters, and contains only alphanumeric characters (order matters):

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 4-8 {{[-c|--charset]}} aA1 {{archive}}`

- Brute-force a password in verbose mode with a length of 3 characters that only contains lowercase characters, `$` and `%`:

`fcrackzip {{[-v|--verbose]}} {{[-b|--brute-force]}} {{[-l|--length]}} 3 {{[-c|--charset]}} a:$% {{archive}}`

- Brute-force a password that contains only lowercase and special characters:

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 4 {{[-c|--charset]}} a! {{archive}}`

- Brute-force a password containing only digits, starting from the password `12345`:

`fcrackzip {{[-b|--brute-force]}} {{[-l|--length]}} 5 {{[-c|--charset]}} 1 {{[-p|--init-password]}} 12345 {{archive}}`

- Crack a password using a wordlist:

`fcrackzip {{[-u|--use-unzip]}} {{[-D|--dictionary]}} {{[-p|--init-password]}} {{wordlist}} {{archive}}`

- Benchmark cracking performance:

`fcrackzip {{[-B|--benchmark]}}`
