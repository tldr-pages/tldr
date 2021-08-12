# croc

> Trimiteți și primiți fișiere ușor și sigur prin orice rețea.
> Mai multe informaţii: <https://github.com/schollz/croc>

- Trimiteți un fișier sau un director:

`croc send {{path/to/file_or_directory}}`

- Trimiteți un fișier sau un director cu o anumită frază de acces:

`croc send --code {{passphrase}} {{path/to/file_or_directory}}`

- Primiți un fișier sau un director pe mașină de primire:

`croc {{passphrase}}`

- Trimiteți și conectați printr-un releu personalizat:

`croc --relay {{ip_to_relay}} send {{path/to/file_or_directory}}`

- Primiți și conectați printr-un releu personalizat:

`croc --relay {{ip_to_relay}} {{passphrase}}`

- Gazda un releu crocodil pe porturile implicite:

`croc relay`

- Afișați parametrii și opțiunile pentru o comandă croc:

`croc {{send|relay}} --help`
