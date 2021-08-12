# vgchange

> Modificați atributele unui grup de volum Logic Volume Manager (LVM).
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://manned.org/vgchange>

- Modificați starea de activare a volumelor logice în toate grupurile de volum:

`sudo vgchange --activate {{y|n}}`

- Modificați starea de activare a volumelor logice în grupul de volum specificat (determinați cu `vgscan`):

`sudo vgchange --activate {{y|n}} {{volume_group}}}`
