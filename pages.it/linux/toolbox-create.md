# toolbox create

> Crea un nuovo contenitore Toolbx.
> Maggiori informazioni: <https://manned.org/toolbox-create>.

- Crea un contenitore Toolbx per una distribuzione specifica:

`toolbox create {{[-d|--distro]}} {{distribuzione}}`

- Crea un contenitore Toolbx per una versione specifica della distribuzione corrente:

`toolbox create {{[-r|--release]}} {{versione}}`

- Crea un contenitore Toolbx con un'immagine personalizzata:

`toolbox create {{[-i|--image]}} {{nome}}`

- Crea un contenitore Toolbx da un'immagine Fedora personalizzata:

`toolbox create {{[-i|--image]}} {{quay.io/fedora/fedora:tag}}`

- Crea un contenitore Toolbx usando l'immagine predefinita per una versione Fedora specifica:

`toolbox create {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{versione}}`
