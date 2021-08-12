# zipalign

> Instrument de aliniere arhivă zip.
> O parte din instrumentele de construire a SDK Android.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/zipalign>

- Aliniați datele unui fișier ZIP pe limitele de 4 octeți:

`zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}`

- Verificați dacă un fișier ZIP este aliniat corect la limitele de 4 octeți și afișați rezultatele într-un mod verbose:

`zipalign -v -c {{4}} {{path/to/input.zip}}`
