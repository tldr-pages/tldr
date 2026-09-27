# fcrackzip

> Fast password cracker for encrypted ZIP archives.
> More information: <https://github.com/hyc/fcrackzip>.

- Perform a dictionary attack using a wordlist:

`fcrackzip {{[-D|--dictionary]}} {{[-p|--init-password]}} {{path/to/wordlist.txt}} {{file.zip}}`

- Perform a dictionary attack with verbose output and verify password guesses:

`fcrackzip {{[-v|--verbose]}} {{[-u|--use-unzip]}} {{[-D|--dictionary]}} {{[-p|--init-password]}} {{path/to/wordlist.txt}} {{file.zip}}`

- Brute-force a password using lowercase letters within a length range:

`fcrackzip {{[-b|--brute-force]}} {{[-c|--charset]}} a {{[-l|--length]}} {{min}}-{{max}} {{file.zip}}`

- Brute-force a password using lowercase letters and digits:

`fcrackzip {{[-b|--brute-force]}} {{[-c|--charset]}} a1 {{file.zip}}`
