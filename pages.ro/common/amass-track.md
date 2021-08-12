# amass track

> Urmăriți diferențele dintre enumerările aceluiași domeniu.
> Mai multe informaţii: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>

- Afișați diferența dintre ultimele două enumerări ale domeniului specificat:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -last 2`

- Afișați diferența dintre un anumit punct în timp și ultima enumerare:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -since {{01/02 15:04:05 2006 MST}}`
