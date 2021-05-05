# hashcat

> Fast and advanced password recovery tool.
> More information: <https://hashcat.net/hashcat/>

- Brute-force attack with default hashcat mask

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 {{hash}}`

- Brute-force attack with a known pattern of 4 digits

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 {{hash}} ?d?d?d?d`

- Brute-force attack with max length of 8 chars using the complete charset (numbers + letters + special chars)

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 --increment {{hash}} ?a?a?a?a?a?a?a?a`

- Dictionary attack using the RockYou wordlist of a Kali Linux box

`hashcat --hash-type {{id_hash_type}} --attack-mode 0 {{hash}} /usr/share/wordlists/rockyou.txt`

- Dictionary + rule based attack using the RockYou wordlist mutated with common password variations

`hashcat --hash-type {{id_hash_type}} --attack-mode 0 -r /usr/share/hashcat/rules/best64.rule {{hash}} /usr/share/wordlists/rockyou.txt`

- Combination attack using the concatenation of words from two different custom dictionaries

`hashcat --hash-type {{id_hash_type}} --attack-mode 1 {{hash}} {{/path/to/dictionary1.txt}} {{/path/to/dictionary2.txt}}`

- Show result of an already-cracked hash

`hashcat --show {{hash}}`
