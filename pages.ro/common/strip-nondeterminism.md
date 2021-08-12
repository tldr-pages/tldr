# strip-nondeterminism

> Un instrument pentru eliminarea informațiilor nedeterministe (de exemplu, marcajele temporale) din fișiere.
> Mai multe informaţii: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>

- Strip informații nedeterministe dintr-un fișier:

`strip-nondeterminism {{path/to/file}}`

- Îndepărtați informațiile nedeterministe dintr-un fișier specificând manual tipul de fișier:

`strip-nondeterminism --type {{filetype}} {{path/to/file}}`

- Îndepărtați informațiile nedeterministe dintr-un fișier; în loc să eliminați marcajele temporale setați-le la marcajul de timp specificat UNIX:

`strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}`
