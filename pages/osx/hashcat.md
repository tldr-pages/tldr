# hashcat

> Password recovery utility
> More information: <https://hashcat.net/wiki/>.

- Wordlist

`hashcat -a 0 -m 400 example400.hash example.dict`

- Wordlist + Rules

`hashcat -a 0 -m 0 example0.hash example.dict -r rules/best64.rule`

- Brute-Force

`hashcat -a 3 -m 0 example0.hash ?a?a?a?a?a?a`

- Combinator

`hashcat -a 1 -m 0 example0.hash example.dict example.dict`

- Association

`hashcat -a 9 -m 500 example500.hash 1word.dict -r rules/best64.rule`
