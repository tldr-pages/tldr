# udisksctl

> Un program de linie de comandă utilizat pentru a interacționa cu procesul de daemon udisksd.
> Mai multe informaţii: <http://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>

- Afișați informații de nivel înalt despre unitățile de disc și dispozitivele de blocare:

`udisksctl status`

- Afișați informații detaliate despre un dispozitiv:

`udisksctl info --block-device {{/dev/sdX}}`

- Afișați informații detaliate despre o partiție de dispozitiv:

`udisksctl info --block-device {{/dev/sdXN}}`

- Montați o partiție de dispozitiv și imprimă punctul de montare:

`udisksctl mount --block-device {{/dev/sdXN}}`

- Demontați o partiție de dispozitiv:

`udisksctl unmount --block-device {{/dev/sdXN}}`

- Monitorizează daemonul pentru evenimente:

`udisksctl monitor`
