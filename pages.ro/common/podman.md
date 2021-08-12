# podman

> Instrument simplu de gestionare pentru păstăi, containere și imagini.
> Podman oferă o linie de comandă comparabilă Docker-CLI. Pur și simplu pune: `alias docker=podman`.
> Mai multe informaţii: <https://github.com/containers/podman/blob/main/commands-demo.md>

- Imprimați informații despre containere:

`podman ps`

- Listează toate containerele (ambele rulează și oprit):

`podman ps --all`

- Porniți unul sau mai multe containere:

`podman start {{container_name}} {{container_id}}`

- Opriți unul sau mai multe containere de funcționare:

`podman stop {{container_name}} {{container_id}}`

- Trageți o imagine dintr-un registru (implicit la Hubul Docker):

`podman pull {{image_name}}:{{image_tag}}`

- Deschideți un înveliș în interiorul unui container deja rulat:

`podman exec --interactive --tty {{container_name}} {{sh}}`

- Scoateți unul sau mai multe recipiente oprite:

`podman rm {{container_name}} {{container_id}}`

- Afișați jurnalele unuia sau mai multor containere și urmați ieșirea jurnal:

`podman logs --follow {{container_name}} {{container_id}}`
