# john

> Cracker de parole.
> Mai multe informaţii: <https://www.openwall.com/john/>

- Crack parola hash:

`john {{path/to/hashes.txt}}`

- Arată parole crăpate:

`john --show {{path/to/hashes.txt}}`

- Afișează parolele fisurate ale utilizatorilor prin identificatorul de utilizator din mai multe fișiere:

`john --show --users={{user_ids}} {{path/to/hashes*}} {{path/to/other/hashes*}}`

- Crack parola hash, folosind o listă de cuvinte personalizată:

`john --wordlist={{path/to/wordlist.txt}} {{path/to/hashes.txt}}`

- Lista formatelor hash disponibile:

`john --list=formats`

- Crack parola hash, folosind un format hash specific:

`john --format={{md5crypt}} {{path/to/hashes.txt}}`

- Crack parola hash, care permite reguli de mangling cuvânt:

`john --rules {{path/to/hashes.txt}}`

- Restaurați o sesiune de cracare întreruptă dintr-un fișier de stat, de exemplu `mycrack.rec`:

`john --restore={{path/to/mycrack.rec}}`
