# partprobe

> Notificați nucleul sistemului de operare al modificărilor tabelei de partiții.
> Mai multe informaţii: <https://manned.org/partprobe>

- Anunțați nucleul sistemului de operare al modificărilor tabelei de partiții:

`sudo partprobe`

- Notificați nucleul modificărilor tabelei de partiții și afișați un rezumat al dispozitivelor și partițiilor acestora:

`sudo partprobe --summary`

- Afișați un rezumat al dispozitivelor și partițiilor acestora, dar nu notificați kernel-ul:

`sudo partprobe --summary --dry-run`
