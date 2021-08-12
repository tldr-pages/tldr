# ctr

> Gestionați containerele și imaginile `container'.
> Mai multe informaţii: <https://containerd.io>

- Listează toate containerele (rulează și oprit):

`ctr containers list`

- Listează toate imaginile:

`ctr images list`

- Trage o imagine:

`ctr images pull {{image}}`

- Etichetează o imagine:

`ctr images tag {{souce_image}}:{{source_tag}} {{target_image}}:{{target_tag}}`
