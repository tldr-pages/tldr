# hashcat

> Instrument de recuperare rapidă și avansată a parolei.
> Mai multe informaţii: <https://manned.org/hashcat>

- Efectuați un atac brute-force (modul 3) cu masca implicită hashcat:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}}`

- Efectuați un atac brute-force (modul 3) cu un model cunoscut de 4 cifre:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}} "{{?d?d?d?d}}"`

- Efectuați un atac brute-force (modul 3) folosind cel mult 8 din toate caracterele ASCII imprimabile:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} --increment {{hash_value}} "{{?a?a?a?a?a?a?a?a}}"`

- Efectuați un atac dicționar (modul 0) folosind lista de cuvinte RockYOU a unei casete Kali Linux:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Efectuați un atac dicționar bazat pe reguli (modul 0) folosind lista de cuvinte RockYOU mutată cu variații comune de parole:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Efectuați un atac combinat (modul 1) utilizând concatenarea cuvintelor din două dicționare personalizate diferite:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{1}} {{hash_value}} {{/path/to/dictionary1.txt}} {{/path/to/dictionary2.txt}}`

- Afișați rezultatul unui hash deja crăpat:

`hashcat --show {{hash_value}}`
