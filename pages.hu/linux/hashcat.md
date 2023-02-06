# hashcat

> Gyors és fejlett jelszó-visszaállító eszköz. További információ: <https://hashcat.net/wiki/doku.php?id=hashcat>.

- Brute-force támadás végrehajtása (3. mód) az alapértelmezett hashcat maszkkal:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}}`

- Brute-force támadás végrehajtása (3. mód) egy ismert 4 számjegyű mintával:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} {{hash_value}} "{{?d?d?d?d}}"`

- Brute-force támadás végrehajtása (3. mód) az összes nyomtatható ASCII karakterből legfeljebb 8 karaktert használva:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{3}} --increment {{hash_value}} "{{?a?a?a?a?a?a?a?a}}"`

- Szótári támadás végrehajtása (0. mód) a Kali Linux doboz RockYou szólistájának használatával:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Szabályalapú szótártámadás végrehajtása (0. mód) a gyakori jelszóváltozatokkal mutált RockYou szólista felhasználásával:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Kombinációs támadás végrehajtása (1. mód) két különböző egyéni szótárból származó szavak összekapcsolásával:

`hashcat --hash-type {{hash_type_id}} --attack-mode {{1}} {{hash_value}} {{/path/to/dictionary1.txt}} {{/path/to/dictionary2.txt}}`

- Egy már feltört hash eredményének megjelenítése:

`hashcat --show {{hash_value}}`
