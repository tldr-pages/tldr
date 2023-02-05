# chntpw

> Egy segédprogram, amely képes a windows registry szerkesztésére, a felhasználói jelszó visszaállítására, a Windows SAM módosításával a felhasználók adminisztrátorrá történő előléptetésére.
> A célgépet a Kali Linuxhoz hasonlóan live cd-vel indítja és emelt jogosultságokkal futtatja.
> További információ [: http://pogostick.net/~pnh/ntpasswd](http://pogostick.net/~pnh/ntpasswd).

- Listázza ki az összes felhasználót a SAM fájlban:

`chntpw -l {{path/to/sam_file}}`

- Szerkessze interaktívan a \[u\]ser-t:

`chntpw -u {{username}} {{path/to/sam_file}}`

- Használja a chntpw \[i\]nteraktívan:

`chntpw -i {{path/to/sam_file}}`
