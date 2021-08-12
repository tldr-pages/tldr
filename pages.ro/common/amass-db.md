# amass db

> Interacționează cu o bază de date Amass.
> Mai multe informaţii: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>

- Lista tuturor enumerărilor efectuate în baza de date:

`amass db -dir {{path/to/database_directory}} -list`

- Afișați rezultatele pentru un index de enumerare specificat și un nume de domeniu:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -show`

- Listează toate subdomeniile găsite ale unui domeniu într-o enumerare:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -names`

- Afișează un rezumat al subdomeniilor găsite într-o enumerare:

`amass db -dir {{path/to/database_directory}} -d {{domain_name}} -enum {{index_from_list}} -summary`
