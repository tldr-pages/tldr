# koji tag-build

> Applica un tag a una o più build.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Applica un tag a una o più build:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}}`

- Non attende l'attività:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}} --nowait`

- Forza l'operazione:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}} --force`

- Mostra aiuto:

`koji tag-build {{[-h|--help]}}`
