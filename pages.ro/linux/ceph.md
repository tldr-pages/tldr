# ceph

> Un sistem de stocare unificat.
> Mai multe informaţii: <https://ceph.io>

- Verificați starea de sănătate a clusterului:

`ceph status`

- Verificați statisticile de utilizare a clusterului:

`ceph df`

- Obțineți statisticile pentru grupurile de plasare într-un cluster:

`ceph pg dump --format {{plain}}`

- Creați un bazin de stocare:

`ceph osd pool create {{pool_name}} {{page_number}}`

- Ștergeți un rezervor de stocare:

`ceph osd pool delete {{pool_name}}`

- Redenumiți un bazin de stocare:

`ceph osd pool rename {{current_name}} {{new_name}}`

- Depozitarea piscinei cu auto-reparare:

`ceph pg repair {{pool_name}}`
