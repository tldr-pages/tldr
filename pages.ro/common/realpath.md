# realpath

> Afișați calea absolută rezolvată pentru un fișier sau un director.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/realpath>

- Afișați calea absolută pentru un fișier sau director:

`realpath {{path/to/file_or_directory}}`

- Necesită ca toate componentele căii să existe:

`realpath --canonicalize-existing {{path/to/file_or_directory}}`

- Rezolvați componentele „..” înainte de simlink-uri:

`realpath --logical {{path/to/file_or_directory}}`

- Dezactivează extinderea simbolului:

`realpath --no-symlinks {{path/to/file_or_directory}}`

- Suprimarea mesajelor de eroare:

`realpath --quiet {{path/to/file_or_directory}}`
