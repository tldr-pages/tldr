# hashcat

> Password cracker.
> More information: <https://hashcat.net/hashcat/>.

- Crack password Wordlist mode:

`hashcat -a 0 -m {{hash-type}} {{hash.txt}} {{wordlist.txt}}`

- Crack password Brute-Force mode:

`hashcat -a 3 -m {{hash-type}} {{hash.txt}} {{charsets}}`

- Output result into file

`hashcat -a 0 -m {{hash-type}} {{hash.txt}} {{wordlist.txt}}  -o {{output.txt}}`

