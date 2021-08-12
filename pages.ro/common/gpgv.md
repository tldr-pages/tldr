# gpgv

> Verificați semnăturile OpenPGP.
> Mai multe informaţii: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>

- Verificați un fișier semnat:

`gpgv {{path/to/file}}`

- Verificați un fișier semnat utilizând o semnătură detașată:

`gpgv {{path/to/signature}} {{path/to/file}}`

- Adăugați un fișier la lista de chei (o singură cheie exportată, de asemenea, contează ca un breloc):

`gpgv --keyring {{./alice.keyring}} {{path/to/signature}} {{path/to/file}}`
