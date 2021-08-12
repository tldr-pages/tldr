# split

> Împărțiți un fișier în bucăți.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/split>

- Împărțiți un fișier, fiecare divizare având 10 linii (cu excepția ultimei divizări):

`split -l {{10}} {{filename}}`

- Împărţiţi un fişier în 5 fişiere. Fișierul este divizat astfel încât fiecare divizare să aibă aceeași dimensiune (cu excepția ultimei divizări):

`split -n {{5}} {{filename}}`

- Împărțiți un fișier cu 512 octeți în fiecare divizare (cu excepția ultimei divizări; utilizați 512k pentru kiloocteți și 512m pentru megaocteți):

`split -b {{512}} {{filename}}`

- Împărțiți un fișier cu cel mult 512 octeți în fiecare divizare, fără a rupe liniile:

`split -C {{512}} {{filename}}`
