# doas

> Execută o comandă ca alt utilizator.
> Mai multe informaţii: <https://man.openbsd.org/doas>

- Rulați o comandă ca root:

`doas {{command}}`

- Rulați o comandă ca alt utilizator:

`doas -u {{user}} {{command}}`

- Lansați shell-ul implicit ca root:

`doas -s`

- Parse un fișier de configurare și verificați dacă executarea unei comenzi ca alt utilizator este permisă:

`doas -C {{config_file}} {{command}}`

- Faceți `doas` să solicite o parolă chiar și după ce a fost furnizată mai devreme:

`doas -L`
