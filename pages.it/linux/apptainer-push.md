# apptainer push

> Invia immagini container a registri remoti.
> Vedi anche: `apptainer-pull`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_push.html>.

- Invia un container alla Container Library:

`apptainer push {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Invia un container a un registro OCI:

`apptainer push {{path/to/immagine.sif}} oras://{{registry/namespace/immagine}}:{{tag}}`

- Invia un container non firmato (salta la verifica della firma):

`apptainer push {{[-U|--allow-unsigned]}} {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Invia un container con una descrizione (solo library):

`apptainer push {{[-D|--description]}} "{{descrizione}}" {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Mostra aiuto:

`apptainer push {{[-h|--help]}}`
