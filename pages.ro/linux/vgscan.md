# vgscan

> Scanați după grupuri de volum pe toate dispozitivele blocate Logic Volume Manager (LVM) acceptate.
> A se vedea, de asemenea, `lvm`, `vgchange`.
> Mai multe informaţii: <https://manned.org/vgscan>

- Scanați după grupuri de volum și imprimați informații despre fiecare grup găsit:

`sudo vgscan`

- Scanați după grupuri de volum și adăugați fișierele speciale în `/dev`, dacă acestea nu există deja, necesare pentru a accesa volumele logice din grupurile găsite:

`sudo vgscan --mknodes`
