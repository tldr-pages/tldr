# distrobox-create

> Maak een Distrobox container. Bekijk ook: `tldr distrobox`.
> De gecreëerde container wordt nauw geïntegreerd met de host, waardoor het delen van de thuismap van de gebruiker, externe opslag, externe USB-apparaten, grafische apps (X11/Wayland) en audio mogelijk is.
> Meer informatie: <https://distrobox.it/usage/distrobox-create>.

- Maak een Distrobox container met behulp van het Ubuntu image:

`distrobox-create {{container_name}} --image {{ubuntu:latest}}`

- Kloon een Distrobox container:

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
