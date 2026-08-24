# mimikatz dpapi

> Interagisce con la Windows Data Protection API (DPAPI).
> Maggiori informazioni: <https://github.com/gentilkiwi/mimikatz>.

- Elenca le chiavi master:

`mimikatz "dpapi::masterkey /list"`

- Decripta un blob DPAPI:

`mimikatz "dpapi::blob /in:blob_file.bin"`

- Recupera le credenziali di Chrome usando DPAPI:

`mimikatz "dpapi::chrome /in:Login Data"`
