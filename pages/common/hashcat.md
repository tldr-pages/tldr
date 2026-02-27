# hashcat

> Fast and advanced password recovery tool.
> More information: <https://hashcat.net/wiki/doku.php?id=hashcat>.

- Perform a brute-force attack (mode 3) with the default hashcat mask:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 {{hash_value}}`

- Perform a brute-force attack (mode 3) with a known pattern of 4 digits:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 {{hash_value}} "{{?d?d?d?d}}"`

- Perform a brute-force attack (mode 3) using at most 8 of all printable ASCII characters:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 3 --increment {{hash_value}} "{{?a?a?a?a?a?a?a?a}}"`

- Perform a dictionary attack (mode 0) using a wordlist:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 0 {{hash_value}} {{path/to/wordlist.txt}}`

- Run a dictionary attack (mode 0) using the specified wordlist, applying rule-based transformations to mutate candidate passwords:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 0 {{[-r|--rules-file]}} {{path/to/file.rule}} {{hash_value}} {{path/to/wordlist.txt}}`

- Perform a combination attack (mode 1) using the concatenation of words from two different custom dictionaries:

`hashcat {{[-m|--hash-type]}} {{hash_type_id}} {{[-a|--attack-mode]}} 1 {{hash_value}} {{path/to/dictionary1.txt}} {{path/to/dictionary2.txt}}`

- Show result of an already cracked hash:

`hashcat --show {{hash_value}}`

- Show all example hashes:

`hashcat --example-hashes`
