# toolbox run

> Esegue un comando in un contenitore Toolbx esistente.
> Vedi anche: `toolbox enter`.
> Maggiori informazioni: <https://manned.org/toolbox-run>.

- Esegue un comando all'interno di un contenitore Toolbx specifico:

`toolbox run {{[-c|--container]}} {{nome_contenitore}} {{comando}}`

- Esegue un comando all'interno di un contenitore Toolbx per una versione specifica di una distribuzione:

`toolbox run {{[-d|--distro]}} {{distribuzione}} {{[-r|--release]}} {{versione}} {{comando}}`

- Esegue `emacs` all'interno di un contenitore Toolbx usando l'immagine predefinita per una versione Fedora specifica:

`toolbox run {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{versione}} {{emacs}}`
