# lsusb

> Visualizza le informazioni su i bus USB e i dispositivi a loro connessi.
> Maggiori informazioni: <https://manned.org/lsusb>.

- Elenca tutti i dispositivi USB disponibili:

`lsusb`

- Visualizza la gerarchia USB come un albero:

`lsusb -t`

- Elenca informazioni prolisse riguardo ai dispositivi USB:

`lsusb --verbose`

- Elenca solamente i dispositivi con un certo id fornitore e ID prodotto:

`lsusb -d {{fornitore}}:{{prodotto}}`
