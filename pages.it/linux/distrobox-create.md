# distrobox-create

> Crea un container Distrobox.
> Il container creato sarà strettamente integrato con l'host, consentendo la condivisione della directory HOME dell'utente, storage esterno, dispositivi USB esterni, app grafiche (X11/Wayland) e audio.
> Vedi anche: `distrobox`.
> Maggiori informazioni: <https://distrobox.it/usage/distrobox-create/>.

- Crea un container Distrobox usando l'immagine Ubuntu:

`distrobox-create {{container_name}} {{[-i|--image]}} {{ubuntu:latest}}`

- Clona un container Distrobox:

`distrobox-create {{[-c|--clone]}} {{container_name}} {{cloned_container_name}}`
