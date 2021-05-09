# hashcat

> Fast and advanced password recovery tool.
> More information: <https://hashcat.net/hashcat/>.

- Perform a brute-force attack (mode 3) with default hashcat mask:

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 {{hash_value}}`

- Perform a brute-force attack (mode 3) with a known pattern of 4 digits:

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 {{hash_value}} {{"?d?d?d?d"}}`

- Perform a brute-force attack (mode 3) using 8 (at most) of all printable ASCII chars with:

`hashcat --hash-type {{id_hash_type}} --attack-mode 3 --increment {{hash_value}} {{"?a?a?a?a?a?a?a?a"}}`

- Perform a dictionary attack (mode 0) using the RockYou wordlist of a Kali Linux box:

`hashcat --hash-type {{id_hash_type}} --attack-mode 0 {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Perform a dictionary + rule based attack (mode 0) using the RockYou wordlist mutated with common password variations:

`hashcat --hash-type {{id_hash_type}} --attack-mode 0 -r {{/usr/share/hashcat/rules/best64.rule}} {{hash_value}} {{/usr/share/wordlists/rockyou.txt}}`

- Perform a combination attack (mode 1) using the concatenation of words from two different custom dictionaries:

`hashcat --hash-type {{id_hash_type}} --attack-mode 1 {{hash_value}} {{/path/to/dictionary1.txt}} {{/path/to/dictionary2.txt}}`

- Show result of an already cracked hash:

`hashcat --show {{hash_value}}`
