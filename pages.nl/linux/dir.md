# dir

> Toon de inhoud van een directory met één regel per bestand, speciale tekens worden weergegeven met backslash-escape-sequenties.
> Werkt als `ls -C --escape`.
> Meer informatie: <https://manned.org/dir>.

- Toon alle bestanden, inclusief verborgen bestanden:

`dir --all`

- Toon bestanden inclusief hun auteur (`-l` is vereist):

`dir -l --author`

- Toon bestanden en sluit degenen uit die overeenkomen met een specifiek patroon:

`dir --hide={{patroon}}`

- Toon subdirectories recursief:

`dir --recursive`

- Toon hulp:

`dir --help`
