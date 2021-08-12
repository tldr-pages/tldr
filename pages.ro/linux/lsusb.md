# lsusb

> Afișați informații despre magistralele USB și dispozitivele conectate la acestea.

- Listează toate dispozitivele USB disponibile:

`lsusb`

- Listează ierarhia USB ca arbore:

`lsusb -t`

- Listați informații detaliate despre dispozitivele USB:

`lsusb --verbose`

- Listați informații detaliate despre un dispozitiv USB:

`lsusb -D {{device}}`

- Listați dispozitivele cu un furnizor specificat și ID-ul produsului numai:

`lsusb -d {{vendor}}:{{product}}`
