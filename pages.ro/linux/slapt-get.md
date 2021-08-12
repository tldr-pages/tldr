# slapt-get

> Un sistem apt like pentru gestionarea pachetelor Slackware.
> Sursele pachetelor trebuie configurate în fișierul slapt-getrc.

- Actualizați lista pachetelor și versiunilor disponibile:

`slapt-get --update`

- Instalați un pachet sau actualizați-l la cea mai recentă versiune disponibilă:

`slapt-get --install {{package_name}}`

- Elimină un pachet:

`slapt-get --remove {{package_name}}`

- Upgrade toate pachetele instalate la cele mai recente versiuni disponibile:

`slapt-get --upgrade`

- Localizați pachetele de interes după numele pachetului, setul de discuri sau versiunea:

`slapt-get --search {{package_name}}`

- Afișați informații despre un pachet:

`slapt-get --show {{package_name}}`
