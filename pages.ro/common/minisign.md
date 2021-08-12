# minisign

> Un instrument simplu mort pentru a semna fișiere și a verifica semnăturile.
> Mai multe informaţii: <https://jedisct1.github.io/minisign/>

- Generați o nouă pereche de chei la locația implicită:

`minisign -G`

- Semnează un fişier:

`minisign -Sm {{path/to/file}}`

- Semnați un fișier, adăugând un comentariu de încredere (semnat) și un comentariu de încredere (nesemnat) în semnătură:

`minisign -Sm {{path/to/file}} -c "{{Untrusted comment}}" -t "{{Trusted comment}}"`

- Verificați un fișier și comentariile de încredere în semnătura sa utilizând fișierul cheie publică specificat:

`minisign -Vm {{path/to/file}} -p {{path/to/publickey.pub}}`

- Verificați un fișier și comentariile de încredere în semnătura sa, specificând o cheie publică ca un Base64 codificat literal:

`minisign -Vm {{path/to/file}} -P "{{public_key_base64}}"`
