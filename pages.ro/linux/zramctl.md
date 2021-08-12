# zramctl

> Configurarea și controlul dispozitivelor zram.
> Utilizați `mkfs` sau `mkswap` pentru a formata dispozitivele zram la partiții.

- Verificați dacă zram este activat:

`lsmod | grep -i zram`

- Activați zram cu un număr dinamic de dispozitive (utilizați `zramctl` pentru a configura dispozitivele în continuare):

`sudo modprobe zram`

- Activați zram cu exact 2 dispozitive:

`sudo modprobe zram num_devices={{2}}`

- Găsiți și inițializați următorul dispozitiv gratuit zram la o unitate virtuală de 2 GB folosind compresie LZ4:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- Lista dispozitivelor inițializate în prezent:

`zramctl`
